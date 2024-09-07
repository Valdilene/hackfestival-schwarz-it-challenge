from openai import OpenAI, Completion
from enum import Enum

MODEL = "gpt-4o-mini"

class PizzaIngredientClass(Enum):
    Sauce = 'sauce ingredient'
    Protein = 'protein'
    Cheese = 'cheese'
    Veggie = 'veggie'
    Topping = 'topping'


def get_pizza_recipe_with_ingredients(ingredients: list[str], openai_client):
    """generate a recepe of pizza, given the ingredients

    Args:
        ingredients (list[str]): list of ingrediends, in human readable form
        openai_client (_type_): OpenAI client

    Returns:
        str: Markdown format for preparing a pizza
    """
    completion = openai_client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": f"What kind of pizza can you make with {', '.join(ingredients)}",
            },
        ],
    )
    return completion.choices[0].message.content


def categorize_ingredient(ingredient: str, openai_client) -> PizzaIngredientClass:
    """gets an ingredient input and classifies it in the following categories:
        'sauce ingredient', 'protein', 'cheese', 'veggie', or 'topping'

    Args:
        ingredient (str): name of the ingredient
        openai_client (OpenAI): open AI client

    Returns:
        PizzaIngredientClass: class for the queried ingredient
    """
    ingredient_classes = " ,".join([e.value for e in PizzaIngredientClass])
    prompt = f"Classify the following ingredient for pizza preparation as one of the following categories: {ingredient_classes}, or 'topping'. Respond with only the category name: '{ingredient}'"
    completion = openai_client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
    )
    return PizzaIngredientClass(completion.choices[0].message.content.strip())

client = OpenAI()

# with open("response.md", "w") as response_file:
#     response_file.write(get_pizza_recipe_with_ingredients(["cheese", "chicken breast", "cherry tomatoes"], client))

print(categorize_ingredient("chicken breast", client))
