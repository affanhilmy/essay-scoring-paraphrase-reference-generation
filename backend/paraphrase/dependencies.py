import torch
from transformers import pipeline, AutoModelWithLMHead, AutoTokenizer

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

def load_paraphrase_model(model_directory):
    tokenizer_gpt = AutoTokenizer.from_pretrained(model_directory)
    model_gpt = AutoModelWithLMHead.from_pretrained(model_directory).to(device)
    generator = pipeline('text-generation', model=model_gpt, tokenizer=tokenizer_gpt, max_length=128, pad_token_id=50256, device=device)
    return model_gpt, tokenizer_gpt, generator

def generate_paraphrase(model_directory, texts, num_return_sequences):
    model_gpt, tokenizer_gpt, generator = load_paraphrase_model(model_directory)
    compiled_paraphrases = []
    for text in texts:
        paraphrases = generator(f'{text}\t', num_return_sequences=num_return_sequences)
        generated_paraphrases = [paraphrase['generated_text'].split("\t")[1].split("\n")[0] for paraphrase in paraphrases]
        compiled_paraphrases.append(generated_paraphrases)
    return compiled_paraphrases
