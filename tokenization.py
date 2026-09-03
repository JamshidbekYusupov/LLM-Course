from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("gpt2")

print(tokenizer.tokenize("I am learnjng LLM and need to find why it is adding G at the beginning of each token"))