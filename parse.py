import sys
from lex import *

# FASE 3 ANALISIS SEMANTICO  20/04/2023
class Parser:
    def __init__(self, lexer):
        self.lexer = lexer

        self.symbols = set()    
        self.labelsDeclared = set() 
        self.labelsGotoed = set() 

        self.curToken = None
        self.peekToken = None
        self.nextToken()
        self.nextToken()   

   
    def checkToken(self, kind):
        return kind == self.curToken.kind

   
    def checkPeek(self, kind):
        return kind == self.peekToken.kind

    def match(self, kind):
        if not self.checkToken(kind):
            self.abort("se esperaba " + kind.name + ", got " + self.curToken.kind.name)
        self.nextToken()

   
    def nextToken(self):
        self.curToken = self.peekToken
        self.peekToken = self.lexer.getToken()
        

  
    def isComparisonOperator(self):
        return self.checkToken(TokenType.GT) or self.checkToken(TokenType.GTEQ) or self.checkToken(TokenType.LT) or self.checkToken(TokenType.LTEQ) or self.checkToken(TokenType.EQEQ) or self.checkToken(TokenType.NOTEQ)

    def abort(self, message):
        sys.exit("Error. " + message)


   

  
    def program(self):
        print("PROGRAMA")

       
        while self.checkToken(TokenType.NEWLINE):
            self.nextToken()

       
        while not self.checkToken(TokenType.EOF):
            self.statement()

      
        for label in self.labelsGotoed:
            if label not in self.labelsDeclared:
                self.abort("NO DECLARADO: " + label)


    def statement(self):
       

        
        if self.checkToken(TokenType.PRINT):
            print("DECLARACION-PRINT")
            self.nextToken()

            if self.checkToken(TokenType.STRING):
               
                self.nextToken()

            else:
              
                self.expression()

       
        elif self.checkToken(TokenType.IF):
            print("DECLARACION-IF")
            self.nextToken()
            self.comparison()

            self.match(TokenType.THEN)
            self.nl()

        
            while not self.checkToken(TokenType.ENDIF):
                self.statement()

            self.match(TokenType.ENDIF)

     
        elif self.checkToken(TokenType.WHILE):
            print("DECLARACION-WHILE")
            self.nextToken()
            self.comparison()

            self.match(TokenType.REPEAT)
            self.nl()

      
            while not self.checkToken(TokenType.ENDWHILE):
                self.statement()

            self.match(TokenType.ENDWHILE)

    
        elif self.checkToken(TokenType.LABEL):
            print("DECLARACION-LABEL")
            self.nextToken()

           
            if self.curToken.text in self.labelsDeclared:
                self.abort("YA EXSITE: " + self.curToken.text)
            self.labelsDeclared.add(self.curToken.text)

            self.match(TokenType.IDENT)

       
        elif self.checkToken(TokenType.GOTO):
            print("DECLARACION-GOTO")
            self.nextToken()
            self.labelsGotoed.add(self.curToken.text)
            self.match(TokenType.IDENT)

    
        elif self.checkToken(TokenType.LET):
            print("DECLARACION-LET")
            self.nextToken()

           
            if self.curToken.text not in self.symbols:
                self.symbols.add(self.curToken.text)

            self.match(TokenType.IDENT)
            self.match(TokenType.EQ)
            
            self.expression()

      
        elif self.checkToken(TokenType.INPUT):
            print("DECLARACION- INPUT")
            self.nextToken()

           
            if self.curToken.text not in self.symbols:
                self.symbols.add(self.curToken.text)

            self.match(TokenType.IDENT)

      
        else:
            self.abort("DECLARACION INVALIDA EN" + self.curToken.text + " (" + self.curToken.kind.name + ")")

      
        self.nl()


  
    def comparison(self):
        print("COMPARACION")

        self.expression()
      
        if self.isComparisonOperator():
            self.nextToken()
            self.expression()
        else:
            self.abort("OPERACION DE COMPARACION EN: " + self.curToken.text)

        
        while self.isComparisonOperator():
            self.nextToken()
            self.expression()


 
    def expression(self):
        print("EXPRESION")

        self.term()

        while self.checkToken(TokenType.PLUS) or self.checkToken(TokenType.MINUS):
            self.nextToken()
            self.term()



    def term(self):
        print("TERM")

        self.unary()

        while self.checkToken(TokenType.ASTERISK) or self.checkToken(TokenType.SLASH):
            self.nextToken()
            self.unary()



    def unary(self):
        print("UNARY")
   
        if self.checkToken(TokenType.PLUS) or self.checkToken(TokenType.MINUS):
            self.nextToken()        
        self.primary()


 
    def primary(self):
        print("PRIMARY (" + self.curToken.text + ")")

        if self.checkToken(TokenType.NUMBER): 
            self.nextToken()
        elif self.checkToken(TokenType.IDENT):
           
            if self.curToken.text not in self.symbols:
                self.abort("Variable de referencia antes de la asignación: " + self.curToken.text)

            self.nextToken()
        else:
         
            self.abort("token inesperado " + self.curToken.text)

    
    def nl(self):
        print("nueva linea")

        
        self.match(TokenType.NEWLINE)
        
        while self.checkToken(TokenType.NEWLINE):
            self.nextToken()