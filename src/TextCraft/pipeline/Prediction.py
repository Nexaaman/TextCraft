from TextCraft.config.configuration import ConfigurationManager
from transformers import AutoTokenizer
from transformers import pipeline

class PredictionPipeline:
    def __init__(self):
        self.config = ConfigurationManager().get_eval_config()

    def predict(self,prompt):
        tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        pipe = pipeline(task="text-generation", model=self.config.model_path, tokenizer=tokenizer,max_length= 1024, truncation= True)
        print("Prompt: ")
        print(prompt)

        output = pipe(f"<s>[INST] {prompt} [/INST]")[0]["generated_text"]
        print("\n Result : ")
        print(output)
        return output