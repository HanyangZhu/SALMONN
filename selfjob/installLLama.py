from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "vicuna-13b-v1.1"  # Replace with actual model path if different
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Save to llama_path
model.save_pretrained(r"C:\Users\38644\PycharmProjects\LLAMA")
tokenizer.save_pretrained(r"C:\Users\38644\PycharmProjects\LLAMA")