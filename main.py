from lexer import Lexer
from parser import Parser
import sys

def main():
    """
    Main entry point to execute EvoLang scripts.
    """
    script_path = sys.argv[1] if len(sys.argv) > 1 else "example_script.evo"
    with open(script_path, "r") as file:
        code = file.read()

    lexer = Lexer()
    tokens = lexer.tokenize(code)

    parser = Parser()
    parser.execute(tokens)

if __name__ == "__main__":
    main()
