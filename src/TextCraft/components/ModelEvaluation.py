from transformers import GPT2Tokenizer, GPT2LMHeadModel
from datasets import load_dataset, load_from_disk, load_metric
import torch
import pandas as pd
from tqdm import tqdm
from TextCraft.entity import ModelEvaluationConfig

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def generate_batched_chunks(self, list_of_elements, batch_size):
        for i in range(0, len(list_of_elements), batch_size):
            yield list_of_elements[i: i+batch_size]
    with torch.no_grad():
        def calculate_metric_on_test_ds(self,dataset, model, tokenizer, 
                                    batch_size=16, device="cuda" if torch.cuda.is_available() else "cpu", 
                                    column_text="text"):
            text_batches = list(self.generate_batch_sized_chunks(dataset[column_text], batch_size))

            for text_batches in tqdm(text_batches, total=len(text_batches)):
                
                inputs = tokenizer(text_batches, max_length=1024,  truncation=True, 
                                padding="max_length", return_tensors="pt")
                
                input_ids = inputs['input_ids'].to(device)
                attention_mask = inputs['attention_mask'].to(device)
                
                labels = input_ids.clone()

                outputs = model(input_ids, attention_mask=attention_mask, labels=labels)
                loss = outputs.loss

                total_loss += loss.item() * input_ids.size(1) 
                total_tokens += input_ids.size(1)    
            perplexity = torch.exp(torch.tensor(total_loss / total_tokens))
            return perplexity.item()
                
    def evaluate(self):
        device = "cuda" if torch.cuda.is_available() else "cpu"
        tokenizer = GPT2Tokenizer.from_pretrained(self.config.tokenizer_path)
        model = GPT2LMHeadModel.from_pretrained(self.config.model_path).to(device)

        dataset_pt = load_from_disk(self.config.data_path)

        # Calculate perplexity on the test dataset
        perplexity = self.calculate_metric_on_test_ds(
            dataset_pt['test'], model, tokenizer, batch_size=2, column_text='text'
        )

        # Save results to a CSV file
        results = {"perplexity": [perplexity]}
        df = pd.DataFrame(results, index=[f'{self.config.model_name}'])
        df.to_csv(self.config.metric_file_name, index=False)