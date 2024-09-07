import ask_chatGPT

from openai import OpenAI

client = OpenAI()

products = ["chicken breast","onion", "beef", "tomatoes"]
classification = ask_chatGPT.classify_ingredients(products, client)
for pair in classification:
    print(pair)
