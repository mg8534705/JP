from transformers import MT5ForConditionalGeneration, MT5Tokenizer

class IncrementalMT5Translator:
    def __init__(self, model_name='google/mt5-small'):
        self.tokenizer = MT5Tokenizer.from_pretrained(model_name)
        self.model = MT5ForConditionalGeneration.from_pretrained(model_name)

    def translate_incremental(self, text_chunk):
        prompt = "translate Japanese to English: " + text_chunk
        input_ids = self.tokenizer.encode(prompt, return_tensors="pt")
        outputs = self.model.generate(input_ids, max_length=128, num_beams=4, early_stopping=True)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
