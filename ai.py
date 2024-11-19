from transformers import pipeline

class AIModel:
    """
    Class to handle AI model interactions using Hugging Face pipeline.
    """
    def __init__(self, model_name):
        self.pipeline = pipeline(model_name)

    def predict(self, prompt):
        """
        Generates a prediction based on the given prompt.
        """
        return self.pipeline(prompt, max_length=50)[0]["generated_text"]
