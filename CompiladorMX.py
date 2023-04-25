from lex import *
from parse import *
import sys

def main():
    #PARA REDUCIR EL ERROR AL CONFUNDIRNOS CON UN GRAN NUMERO DE LINEAS Y  OPTIMIZAR UN POCO DECIDIMOS
    #REALIZAR NUESTROS CODIGOS EN PARTES Y DESPUES REUNIRLOS EN ESTA FUNCION PRINCIPAL, IMPORTANDO
    #NUESTRAS CLASES DE NUESTROS OTROS PROGRAMA,MANEJADOS COMO ARCHIVOS 
    print("ESIMIO COMPILER")

    if len(sys.argv) != 2:
        sys.exit("Error:compilador necesita archivo fuente como fuente.")
    with open(sys.argv[1], 'r') as inputFile:
        source = inputFile.read()
        
    lexer = Lexer(source)
    parser = Parser(lexer)

    parser.program() 
    print("Parsing completado.")

main()