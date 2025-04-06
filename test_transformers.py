from transformers import pipeline

pipe = pipeline("text-generation", model="microsoft/DialoGPT-small")
res = pipe("Hello, how are you?")
print(res)
