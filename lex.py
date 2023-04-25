import sys
import enum

# COMIENZA NUESTRO ANALISIS LEXICO CON NUESTRA CLASE LEXER 12/04/2023
class Lexer:
    def __init__(self, source):
        self.source = source + '\n' 
        self.curChar = '' 
        self.curPos = -1   
        self.nextChar()

   
    def nextChar(self):
        self.curPos += 1
        if self.curPos >= len(self.source):
            self.curChar = '\0'  
        else:
            self.curChar = self.source[self.curPos]

   
    def peek(self):
        if self.curPos + 1 >= len(self.source):
            return '\0'
        return self.source[self.curPos+1]

    
    def abort(self, message):
        sys.exit("ERROR LEXICO. " + message)


    def getToken(self):
        self.skipWhitespace()
        self.skipComment()
        token = None

      #----------------------------------------------------------------------------1FIN--- 13/04/2023
      #13/04/2023
        if self.curChar == '+':
            token = Token(self.curChar, TokenType.PLUS)
        elif self.curChar == '-':
            token = Token(self.curChar, TokenType.MINUS)
        elif self.curChar == '*':
            token = Token(self.curChar, TokenType.ASTERISK)
        elif self.curChar == '/':
            token = Token(self.curChar, TokenType.SLASH)
        elif self.curChar == '=':
           
            if self.peek() == '=':
                lastChar = self.curChar
                self.nextChar()
                token = Token(lastChar + self.curChar, TokenType.EQEQ)
            else:
                token = Token(self.curChar, TokenType.EQ)
        elif self.curChar == '>':
           
            if self.peek() == '=':
                lastChar = self.curChar
                self.nextChar()
                token = Token(lastChar + self.curChar, TokenType.GTEQ)
            else:
                token = Token(self.curChar, TokenType.GT)
        elif self.curChar == '<':
            
            if self.peek() == '=':
                lastChar = self.curChar
                self.nextChar()
                token = Token(lastChar + self.curChar, TokenType.LTEQ)
            else:
                token = Token(self.curChar, TokenType.LT)
        elif self.curChar == '!':
            if self.peek() == '=':
                lastChar = self.curChar
                self.nextChar()
                token = Token(lastChar + self.curChar, TokenType.NOTEQ)
            else:
                self.abort("NO ES !=, ES !" + self.peek())

        elif self.curChar == '\"':
            
            self.nextChar()
            startPos = self.curPos

            while self.curChar != '\"':
                
                
                if self.curChar == '\r' or self.curChar == '\n' or self.curChar == '\t' or self.curChar == '\\' or self.curChar == '%':
                    self.abort("CARATER ERRONEO EN LA CADENA.")
                self.nextChar()

            tokText = self.source[startPos : self.curPos] 
            token = Token(tokText, TokenType.STRING)

        elif self.curChar.isdigit():
           
            
            startPos = self.curPos
            while self.peek().isdigit():
                self.nextChar()
            if self.peek() == '.': 
                self.nextChar()

                
                if not self.peek().isdigit(): 
                    
                    self.abort("CARACTER DIFERENTE EN LOS NUMEROS.")
                while self.peek().isdigit():
                    self.nextChar()

            tokText = self.source[startPos : self.curPos + 1] 
            token = Token(tokText, TokenType.NUMBER)
        elif self.curChar.isalpha():
            
            
            startPos = self.curPos
            while self.peek().isalnum():
                self.nextChar()

           
            tokText = self.source[startPos : self.curPos + 1] 
            keyword = Token.checkIfKeyword(tokText)
            if keyword == None: 
                token = Token(tokText, TokenType.IDENT)
            else:   
                token = Token(tokText, keyword)
        elif self.curChar == '\n':
           
            token = Token('\n', TokenType.NEWLINE)
        elif self.curChar == '\0':
             
            token = Token('', TokenType.EOF)
        else:
           
            self.abort("TOKEN DESCONOCIDO: " + self.curChar)

        self.nextChar()
        return token

    
    def skipWhitespace(self):
        while self.curChar == ' ' or self.curChar == '\t' or self.curChar == '\r':
            self.nextChar()

    def skipComment(self):
        if self.curChar == '#':
            while self.curChar != '\n':
                self.nextChar()
  


class Token:   
    def __init__(self, tokenText, tokenKind):
        self.text = tokenText   
        self.kind = tokenKind   

    @staticmethod
    def checkIfKeyword(tokenText):
        for kind in TokenType:
            
            if kind.name == tokenText and kind.value >= 100 and kind.value < 200:
                return kind
        return None
 #FIN DE NUESTRO ANALISIS LEXICO 21/04/2023

#DEFINICION DE NUESTRAS PALABRAS RESERVADAS Y OPERADORES BASICOS INICIO13/04/2023- FIN 23/04/2023
class TokenType(enum.Enum):
    EOF = -1
    NEWLINE = 0
    NUMBER = 1
    IDENT = 2
    STRING = 3
    # RESERVADAS
    LABEL = 101
    GOTO = 102
    PRINT = 103
    INPUT = 104
    LET = 105
    IF = 106
    THEN = 107
    ENDIF = 108
    WHILE = 109
    REPEAT = 110
    ENDWHILE = 111
    # OPERADORES
    EQ = 201  
    PLUS = 202
    MINUS = 203
    ASTERISK = 204
    SLASH = 205
    EQEQ = 206
    NOTEQ = 207
    LT = 208
    LTEQ = 209
    GT = 210
    GTEQ = 211