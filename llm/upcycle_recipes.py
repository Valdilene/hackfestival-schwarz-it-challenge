from dataclasses import dataclass
from enum import Enum
from collections import defaultdict
from itertools import zip_longest

class PizzaIngredientCategory(Enum):
    Sauce = "sauce ingredient"
    Protein = "protein"
    Cheese = "cheese"
    Veggie = "vegetable"
    Topping = "topping"

@dataclass
class Ingredient:
    name: str
    quantity_g: str
    category: PizzaIngredientCategory = None

@dataclass
class Recipe:
    ingredients: list[Ingredient]
    name: str = None
    marketing_motto: str = None
    instructions: list = None
    
def split_ingredients_over_recipes(ingredients: list[Ingredient]) -> list[Recipe]:
    """Creates a list of recipes that include equal quantities of maximum two ingredients from
    each category such that all categories are consumed.
    
    The remaining categories are put into recipes that have equal quantities of maximum two ingredients
    of a category in N-1 categories and so on. 

    Args:
        ingredients (list[Ingredient]): _description_

    Returns:
        list[Recipe]: _description_
    """
    # Step 1: Group ingredients by category
    categorized_ingredients = defaultdict(list)
    
    for ingredient in ingredients:
        categorized_ingredients[ingredient.category].append(ingredient)

    # Step 2: Create recipes and add up to two ingredients from each category
    recipes = []
    max_ingredients_per_category = 2

    # Create recipes with ingredients grouped into N-1 categories and so on
    while any(categorized_ingredients.values()):
        recipe_ingredients = []
        
        # Step 3: Add up to two ingredients from each category to a recipe
        for category, ing_list in categorized_ingredients.items():
            # Take up to two ingredients from each category
            if ing_list:
                ingredients_to_add = ing_list[:max_ingredients_per_category]
                recipe_ingredients.extend(ingredients_to_add)
                
                # Remove the used ingredients from the category
                categorized_ingredients[category] = ing_list[max_ingredients_per_category:]
        
        # Step 4: Create the recipe
        recipe = Recipe(ingredients=recipe_ingredients)
        recipes.append(recipe)

    return recipes