import json
from ask_chatGPT import add_instructions_to_recipe, classify_ingredients
from upcycle_recipes import Ingredient, split_ingredients_over_recipes
from openai import OpenAI

client = OpenAI()

test_data = json.load("test_data.json")

ingredients = [Ingredient(name=i["name"], quantity_g=i["quantity_g"]) for i in test_data]

classified_ingredients = classify_ingredients(ingredients, client)

recipes = split_ingredients_over_recipes(ingredients)

for recipe in recipes:
    recipes = add_instructions_to_recipe(recipe)
    with open(f"test_result/{recipe.name}.md")