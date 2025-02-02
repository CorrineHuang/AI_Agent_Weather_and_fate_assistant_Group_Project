from transformers import AutoModelForCausalLM, AutoTokenizer

# Load the DeepSeek local model (modify path as needed)
model_path = "/path/to/deepseek/model"  

tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path)

def generate_analysis(prompt):
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs, max_length=200)
    result = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return result
