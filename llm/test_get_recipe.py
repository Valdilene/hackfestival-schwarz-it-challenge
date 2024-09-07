import ask_chatGPT

from openai import OpenAI

from upcycle_recipes import Ingredient, Recipe

client = OpenAI()

with open("response.md", "w") as response_file:
    ingredients = [Ingredient(i, 0) for i in ["cheese", "chicken breast", "cherry tomatoes"]]
    recipe = Recipe(ingredients=ingredients)
    recipe = ask_chatGPT.add_instructions_to_recipe(recipe, client)
    print(recipe.name)
    print(recipe.instructions_md)


