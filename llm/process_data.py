import json
from ask_chatGPT import add_instructions_to_recipe, classify_ingredients
from upcycle_recipes import Ingredient, split_ingredients_over_recipes
from openai import OpenAI


def process_foods(ingredients):
    openai_client = OpenAI()
    classified_ingredients = classify_ingredients(ingredients, openai_client)

    recipes = split_ingredients_over_recipes(classified_ingredients)

    for recipe in recipes:
        recipes = add_instructions_to_recipe(recipe, openai_client)
        with open(f"test_result/{recipe.name}.md", "w") as recipe_file:
            recipe_file.write(f"# {recipe.name}")
            recipe_file.write("\n\n## Ingredients:\n* ")
            recipe_file.write(
                "\n* ".join([f"{i.name}[{i.quantity_g}]" for i in recipe.ingredients])
            )
            recipe_file.write("\n\n## Steps:\n* ")
            recipe_file.write("\n* ".join(recipe.instructions))
            recipe_file.write("\n\n# Machine Readable Data\n")
            recipe_file.write("\n```json\n")
            recipe_file.write(
                json.dumps(
                    dict(
                        name=recipe.name,
                        ingredients=[
                            dict(ingredient=i.name, quantity=i.quantity_g)
                            for i in recipe.ingredients
                        ],
                        steps=recipe.instructions,
                    ),
                    indent=4,
                )
            )
            recipe_file.write("\n```\n")
