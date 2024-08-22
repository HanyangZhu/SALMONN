from transformers import AutoModel, AutoTokenizer

beats_path = r'C:\Users\38644\PycharmProjects\beats'  # Replace with your actual path

# Download the model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("microsoft/beats-finetuned-as2m-cpt2", cache_dir=beats_path)
model = AutoModel.from_pretrained("microsoft/beats-finetuned-as2m-cpt2", cache_dir=beats_path)