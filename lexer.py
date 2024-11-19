import re

class Lexer:
    """
    Lexer class to tokenize EvoLang code.
    """
    def tokenize(self, code):
        tokens = []
        lines = code.split("\n")
        for line in lines:
            line = line.strip()
            if line.startswith("model = load_model"):
                tokens.append({"type": "LOAD_MODEL", "value": line})
            elif ".predict(" in line:
                tokens.append({"type": "PREDICT", "value": line})
            elif line.startswith("print"):
                tokens.append({"type": "PRINT", "value": line})
        return tokens
