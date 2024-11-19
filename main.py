from lexer import Lexer
from parser import Parser

def main():
    """
    Main entry point to execute EvoLang scripts.
    """
    # Load the EvoLang script
    with open("example_script.evo", "r") as file:
        code = file.read()

    lexer = Lexer()
    tokens = lexer.tokenize(code)

    parser = Parser()
    parser.execute(tokens)

if __name__ == "__main__":
    main()
