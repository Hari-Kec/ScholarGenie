from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM

model = None
tokenizer = None
pipe = None

def load_model():
    global model, tokenizer, pipe
    model = AutoModelForCausalLM.from_pretrained("models/gemma-3n")
    tokenizer = AutoTokenizer.from_pretrained("models/gemma-3n")
    pipe = pipeline("text-generation", model=model, tokenizer=tokenizer)

def infer(prompt: str):
    return pipe(prompt, max_new_tokens=150)[0]['generated_text']