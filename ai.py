try:
    from transformers import pipeline
except Exception:
    pipeline = None

class AIModel:
    """
    Class to handle AI model interactions using Hugging Face pipeline.
    If transformers is not available, falls back to a stub that echoes the prompt.
    """
    def __init__(self, model_name):
        self.model_name = model_name
        self._use_pipeline = pipeline is not None
        self._pipeline = None
        self._error = None
        if self._use_pipeline:
            try:
                self._pipeline = pipeline(model_name)
            except Exception as e:
                self._use_pipeline = False
                self._pipeline = None
                self._error = str(e)
        else:
            self._error = "transformers not installed"

    def predict(self, prompt):
        """
        Generates a prediction based on the given prompt.
        """
        if self._use_pipeline and self._pipeline is not None:
            try:
                outputs = self._pipeline(prompt, max_new_tokens=50)
                if isinstance(outputs, list) and len(outputs) > 0:
                    first = outputs[0]
                    if isinstance(first, dict) and "generated_text" in first:
                        return first["generated_text"]
                return str(outputs)
            except Exception as e:
                return f"[AI error: {e}]"
        return f"[{self.model_name} stub] {prompt}"
