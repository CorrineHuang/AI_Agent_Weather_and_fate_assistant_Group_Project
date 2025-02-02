import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig


# MODEL_NAME = "deepseek-ai/DeepSeek-R1-Distill-Qwen-14B"
MODEL_NAME = 'gpt2'
# Set up bitsandbytes quantization configuration
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,  # Load model in 4-bit precision to reduce memory usage
    bnb_4bit_compute_dtype=torch.float16,  # Compute in float16
    bnb_4bit_quant_type="nf4",  # Normal Float 4 quantization
    bnb_4bit_use_double_quant=False,  # Disable double quantization for stability
)

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

# Load model with quantization config
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    quantization_config=bnb_config,  # Use quantized configuration
    device_map="auto",  # Automatically distribute across GPUs
)

# Move to GPU if available
device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)

def generate_analysis(prompt, max_length=200):
    """Generate text from DeepSeek model based on input prompt."""
    inputs = tokenizer(prompt, return_tensors="pt").to(device)
    outputs = model.generate(**inputs, max_length=max_length)
    result = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return result
