
class PromptGenerator:
    """A class to generate prompts for analyzing text and extracting question-answer pairs."""
    
    def __init__(self,text_chunk,data_type):
        # Example template for question-answer extraction
        self.data_type = data_type
        self.text_chunk = text_chunk

    
    def __call__(self, text_chunk, data_type):
        """Generates a prompt for analyzing a chunk of text based on the specified data type."""
        if data_type == "json":
            return f"""
                Analyze the text: {text_chunk}

                Extract key information and formulate a list of question-answer pairs in JSON format.

                **Example:**

                "question": "What is formed when dilute sulphuric acid is added to zinc granules?",
                "answer": "Change in state, change in colour, evolution of a gas, change in temperature."
            """
        elif data_type == "csv":
            return f"""
                Analyze the text: {text_chunk}

                Extract key information and formulate a list of question-answer pairs in CSV format.

                **Example:**
                question,answer
                What is formed when dilute sulphuric acid is added to zinc granules?,Change in state, change in colour, evolution of a gas, change in temperature.
            """
        else:
            raise ValueError("Currently, only 'json' and 'csv' data types are supported for prompt generation.")
