import json
from ask_chatGPT import add_instructions_to_recipe, classify_ingredients
from upcycle_recipes import Ingredient, split_ingredients_over_recipes
from openai import OpenAI

openai_client = OpenAI()

with open("test_data.json") as test_data_file:
    test_data = json.load(test_data_file)

ingredients = [Ingredient(name=i["name"], quantity_g=i["quantity_g"]) for i in test_data]

classified_ingredients = classify_ingredients(ingredients, openai_client)

recipes = split_ingredients_over_recipes(ingredients)

for recipe in recipes:
    recipes = add_instructions_to_recipe(recipe, openai_client)
    with open(f"test_result/{recipe.name}.md", "w") as recipe_file:
        recipe_file.write("# Ingredients:\n* ")
        recipe_file.write("\n* ".join([f"{i.name}[{i.quantity_g}]" for i in recipe.ingredients]))
        recipe_file.write("\n# Steps:\n* ")
        recipe_file.write("\n* ".join(recipe.instructions))

        