import sys
from lex import *


# El objeto Parser realiza el seguimiento del token actual, verifica si el código coincide con la gramática y emite código a lo largo del proceso.
class Parser:
    def __init__(self, lexer, emitter):
        self.lexer = lexer
        self.emitter = emitter

        self.symbols = set()  # Todas las variables declaradas hasta ahora.
        self.labelsDeclared = set()  # Mantener un registro de todas las etiquetas declaradas.
        self.labelsGotoed = set()  # Todas las etiquetas a las que se hace "goto", para saber si existen o no.

        self.curToken = None
        self.peekToken = None
        self.nextToken()
        self.nextToken()  # Llamarlo dos veces para inicializar el token actual y el token siguiente.

    # Devuelve verdadero si el token actual coincide.
    def checkToken(self, kind):
        return kind == self.curToken.kind

    # Devuelve verdadero si el siguiente token coincide.
    def checkPeek(self, kind):
        return kind == self.peekToken.kind

    # Intenta hacer coincidir el token actual. Si no lo consigue, muestra un error. Avanza al token actual.
    def match(self, kind):
        if not self.checkToken(kind):
            self.abort("Se esperaba " + kind.name + ", se obtuvo " + self.curToken.kind.name)
        self.nextToken()

    # Avanza al siguiente token.
    def nextToken(self):
        self.curToken = self.peekToken
        self.peekToken = self.lexer.getToken()
        # No es necesario preocuparse por pasar el final de archivo (EOF), el analizador léxico se encarga de eso.

    # Devuelve verdadero si el token actual es un operador de comparación.
    def isComparisonOperator(self):
        return (
            self.checkToken(TokenType.GT)
            or self.checkToken(TokenType.GTEQ)
            or self.checkToken(TokenType.LT)
            or self.checkToken(TokenType.LTEQ)
            or self.checkToken(TokenType.EQEQ)
            or self.checkToken(TokenType.NOTEQ)
        )

    def abort(self, message):
        sys.exit("¡Error! " + message)

    # Reglas de producción.

    # program ::= {statement}
        # program ::= {statement}
    def program(self):
        self.emitter.headerLine("#include <stdio.h>")
        self.emitter.headerLine("int main(void){")
        
        # Since some newlines are required in our grammar, need to skip the excess.
        while self.checkToken(TokenType.NEWLINE):
            self.nextToken()

        # Parse all the statements in the program.
        while not self.checkToken(TokenType.EOF):
            self.statement()

        # Wrap things up.
        self.emitter.emitLine("return 0;")
        self.emitter.emitLine("}")

        # Check that each label referenced in a GOTO is declared.
        for label in self.labelsGotoed:
            if label not in self.labelsDeclared:
                self.abort("Attempting to GOTO to undeclared label: " + label)

    # Una de las siguientes declaraciones...
    def statement(self):
        # Verifica el primer token para determinar qué tipo de declaración es.

        # "PRINT" (expression | string)
        if self.checkToken(TokenType.PRINT):
            self.nextToken()

            if self.checkToken(TokenType.STRING):
                # Es una cadena simple, así que se imprime.
                self.emitter.emitLine('printf("' + self.curToken.text + '\\n");')
                self.nextToken()

            else:
                # Se espera una expresión y se imprime el resultado como un número de punto flotante.
                self.emitter.emit('printf("%' + '.2f\\n", (float)(')
                self.expression()
                self.emitter.emitLine('));')

        # "IF" comparison "THEN" block "ENDIF"
        elif self.checkToken(TokenType.IF):
            self.nextToken()
            self.emitter.emit("if (")
            self.comparison()

            self.match(TokenType.THEN)
            self.nl()
            self.emitter.emitLine(") {")

            # Cero o más declaraciones en el cuerpo.
            while not self.checkToken(TokenType.ENDIF):
                self.statement()

            self.match(TokenType.ENDIF)
            self.emitter.emitLine("}")

        # "WHILE" comparison "REPEAT" block "ENDWHILE"
        elif self.checkToken(TokenType.WHILE):
            self.nextToken()
            self.emitter.emit("while (")
            self.comparison()

            self.match(TokenType.REPEAT)
            self.nl()
            self.emitter.emitLine(") {")

            # Cero o más declaraciones en el cuerpo del bucle.
            while not self.checkToken(TokenType.ENDWHILE):
                self.statement()

            self.match(TokenType.ENDWHILE)
            self.emitter.emitLine("}")

        # "LABEL" ident
        elif self.checkToken(TokenType.LABEL):
            self.nextToken()

            # Asegurarse de que esta etiqueta no exista ya.
            if self.curToken.text in self.labelsDeclared:
                self.abort("La etiqueta ya existe: " + self.curToken.text)
            self.labelsDeclared.add(self.curToken.text)

            self.emitter.emitLine(self.curToken.text + ":")
            self.match(TokenType.IDENT)

        # "GOTO" ident
        elif self.checkToken(TokenType.GOTO):
            self.nextToken()
            self.labelsGotoed.add(self.curToken.text)
            self.emitter.emitLine("goto " + self.curToken.text + ";")
            self.match(TokenType.IDENT)

        # "LET" ident = expression
        elif self.checkToken(TokenType.LET):
            self.nextToken()

            # Comprobar si la ident ya existe en la tabla de símbolos. Si no existe, se declara.
            if self.curToken.text not in self.symbols:
                self.symbols.add(self.curToken.text)
                self.emitter.headerLine("float " + self.curToken.text + ";")

            self.emitter.emit(self.curToken.text + " = ")
            self.match(TokenType.IDENT)
            self.match(TokenType.EQ)

            self.expression()
            self.emitter.emitLine(";")

        # "INPUT" ident
        elif self.checkToken(TokenType.INPUT):
            self.nextToken()

            # Si la variable no existe, se declara.
            if self.curToken.text not in self.symbols:
                self.symbols.add(self.curToken.text)
                self.emitter.headerLine("float " + self.curToken.text + ";")

            # Emitir scanf pero también validar la entrada. Si es inválida, se establece la variable en 0 y se limpia la entrada.
            self.emitter.emitLine(
                'if (0 == scanf("%f", &' + self.curToken.text + ')) {'
            )
            self.emitter.emitLine(self.curToken.text + " = 0;")
            self.emitter.emit('scanf("%')
            self.emitter.emitLine('*s");')
            self.emitter.emitLine("}")
            self.match(TokenType.IDENT)

        # ¡Esto no es una declaración válida! ¡Error!
        else:
            self.abort(
                "Declaración no válida en " + self.curToken.text + " (" + self.curToken.kind.name + ")"
            )

        # Nueva línea.
        self.nl()

    # comparison ::= expression (("==" | "!=" | ">" | ">=" | "<" | "<=") expression)+
    def comparison(self):
        self.expression()
        # compara una expresion con un operador
        if self.isComparisonOperator():
            self.emitter.emit(self.curToken.text)
            self.nextToken()
            self.expression()
        # 
        while self.isComparisonOperator():
            self.emitter.emit(self.curToken.text)
            self.nextToken()
            self.expression()


    # expression ::= term {( "-" | "+" ) term}
    def expression(self):
        self.term()
        
        while self.checkToken(TokenType.PLUS) or self.checkToken(TokenType.MINUS):
            self.emitter.emit(self.curToken.text)
            self.nextToken()
            self.term()


    # term ::= unary {( "/" | "*" ) unary}
    def term(self):
        self.unary()
      
        while self.checkToken(TokenType.ASTERISK) or self.checkToken(TokenType.SLASH):
            self.emitter.emit(self.curToken.text)
            self.nextToken()
            self.unary()


    # unary ::= ["+" | "-"] primary
    def unary(self):
        # Optional unary +/-
        if self.checkToken(TokenType.PLUS) or self.checkToken(TokenType.MINUS):
            self.emitter.emit(self.curToken.text)
            self.nextToken()        
        self.primary()


    # primary ::= number | ident
    def primary(self):
        if self.checkToken(TokenType.NUMBER): 
            self.emitter.emit(self.curToken.text)
            self.nextToken()
        elif self.checkToken(TokenType.IDENT):
          
            if self.curToken.text not in self.symbols:
                self.abort("Referencing variable before assignment: " + self.curToken.text)

            self.emitter.emit(self.curToken.text)
            self.nextToken()
        else:
            # Error!
            self.abort("Unexpected token at " + self.curToken.text)

    # nl ::= '\n'+
    def nl(self):

        self.match(TokenType.NEWLINE)
    
        while self.checkToken(TokenType.NEWLINE):
            self.nextToken()