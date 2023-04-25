from lex import *
from parse import *
import sys

def main():
    print("Compilador ESIMIO")

    if len(sys.argv) != 2:
        sys.exit("Error:compilador necesita archivo fuente como fuente.")
    with open(sys.argv[1], 'r') as inputFile:
        source = inputFile.read()

    # inizializa el lexico y el parsing
    lexer = Lexer(source)
    parser = Parser(lexer)

    parser.program() # empieza el parsing
    print("Parsing completado.")

main()