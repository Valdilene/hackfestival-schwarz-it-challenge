import json
from openai import OpenAI, Completion
from upcycle_recipes import Ingredient, PizzaIngredientCategory, Recipe

OPEN_AI_MODEL = "gpt-4o-mini"


def add_instructions_to_recipe(recipe: Recipe, openai_client: OpenAI):
    """generate a recepe of pizza, given the ingredients

    Args:
        ingredients (list[str]): list of ingrediends, in human readable form
        openai_client (_type_): OpenAI client

    Returns:
        str: Markdown format for preparing a pizza
    """
    ingredients = [i.name for i in  recipe.ingredients]
    completion = openai_client.chat.completions.create(
        model=OPEN_AI_MODEL,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": (
                    "Provide a pizza recipe you can make with the ingredients below and a creative name for it."
                    "Respond **only** with the output in raw JSON format without any additional text or markdown. "
                    "the output has to be in the format name: creative_name, recipe: recipe instructions as a list"
                    f"Ingredients {', '.join(ingredients)}"

                ),
            },
        ],
    )
    recipe_response = json.loads(completion.choices[0].message.content)
    recipe.instructions_md = recipe_response["recipe"]
    recipe.name = recipe_response["name"]
    return recipe


def classify_ingredients(ingredients: list[Ingredient], openai_client: OpenAI) -> list[Ingredient]:
    """gets an ingredient input and classifies it in the following categories:
        'sauce ingredient', 'protein', 'cheese', 'veggie', or 'topping'

    Args:
        ingredient (str): name of the ingredient. One name ca only occur once
        openai_client (OpenAI): open AI client

    Returns:
        PizzaIngredientClass: class for the queried ingredient
    """
    ingredient_classes = " ,".join([e.value for e in PizzaIngredientCategory])
    
    # map all ingredient objects by name
    mapped_ingredients = {i.name: i for i in ingredients}
    print(ingredient_classes)
    prompt = (
        f"Classify the following ingredients for pizza preparation as one of the following categories: "
        "{ingredient_classes}"
        "Respond **only** with the output in raw JSON format without any additional text or markdown. "
        "the output has to be in the format ingredient: class"
        f"Ingredients: {[i.name for i in ingredients]}"
    )
    completion = openai_client.chat.completions.create(
        model=OPEN_AI_MODEL,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
    )
    categories = completion.choices[0].message.content.strip()
    parsed_categories = json.loads(categories)
    for ingredient_name, category in parsed_categories.items():
        mapped_ingredients[ingredient_name].category = category
        
    return [v for k, v in mapped_ingredients]
