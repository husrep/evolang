import re

class Lexer:
    """
    Lexer class to tokenize EvoLang code.
    """
    def __init__(self):
        self.pattern_load_model = re.compile(r'^(?P<var>\w+)\s*=\s*load_model\(\s*"(?P<model>[^"]+)"\s*\)\s*$')
        self.pattern_assign_predict = re.compile(r'^(?P<var>\w+)\s*=\s*(?P<modelvar>\w+)\.predict\(\s*prompt\s*=\s*"(?P<prompt>[^"]*)"\s*\)\s*$')
        self.pattern_predict_no_assign = re.compile(r'^(?P<modelvar>\w+)\.predict\(\s*prompt\s*=\s*"(?P<prompt>[^"]*)"\s*\)\s*$')
        self.pattern_print_string = re.compile(r'^print\(\s*"(?P<text>[^"]*)"\s*\)\s*$')
        self.pattern_print_var = re.compile(r'^print\(\s*(?P<var>\w+)\s*\)\s*$')

    def tokenize(self, code):
        tokens = []
        lines = code.split("\n")
        for raw_line in lines:
            line = raw_line.strip()
            if not line or line.startswith("#"):
                continue

            match = self.pattern_load_model.match(line)
            if match:
                tokens.append({
                    "type": "LOAD_MODEL",
                    "var": match.group("var"),
                    "model_name": match.group("model")
                })
                continue

            match = self.pattern_assign_predict.match(line)
            if match:
                tokens.append({
                    "type": "ASSIGN_PREDICT",
                    "var": match.group("var"),
                    "model_var": match.group("modelvar"),
                    "prompt": match.group("prompt")
                })
                continue

            match = self.pattern_predict_no_assign.match(line)
            if match:
                tokens.append({
                    "type": "PREDICT",
                    "model_var": match.group("modelvar"),
                    "prompt": match.group("prompt")
                })
                continue

            match = self.pattern_print_string.match(line)
            if match:
                tokens.append({
                    "type": "PRINT_STRING",
                    "value": match.group("text")
                })
                continue

            match = self.pattern_print_var.match(line)
            if match:
                tokens.append({
                    "type": "PRINT_VAR",
                    "var": match.group("var")
                })
                continue

            raise SyntaxError(f"Unrecognized line: {line}")

        return tokens
