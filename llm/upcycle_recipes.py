from dataclasses import dataclass
from enum import Enum
from collections import defaultdict

# Does not need to be equal
RECIPE_QUANTITY_MARGIN = 0.5

class PizzaIngredientCategory(Enum):
    Sauce = "sauce ingredient"
    Protein = "protein"
    Cheese = "cheese"
    Veggie = "vegetable"
    Fruit = "fruit"
    Topping = "topping"
    Spice = "spice"
    No = "not for pizza"

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


def remove_ingredient_by_name(ingredients: list[Ingredient], name: str) -> list[Ingredient]:
    # Filter out the ingredient that matches the given name
    return [ingredient for ingredient in ingredients if ingredient.name != name]

def pop_first_ingredient_in_range(ingredients, min, max):
    for candidate_i in ingredients:
        if min <= float(candidate_i.quantity_g) <= max:
            ingredients = remove_ingredient_by_name(ingredients, candidate_i.name)
            print("matched")
            return candidate_i
    return None

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
    categorized_ingredients = defaultdict(list)
    for ingredient in ingredients:
        categorized_ingredients[ingredient.category].append(ingredient)

    recipes = []

    # Create recipes with ingredients grouped into N-1 categories and so on
    while any(categorized_ingredients.values()) and any(ingredients):
        recipe_ingredients = []
        
        # get the smallest ingredient from all ingredients
        lowest_quantity_ingredient = min(ingredients, key=lambda ingredient: ingredient.quantity_g)
        ingredients = remove_ingredient_by_name(ingredients, lowest_quantity_ingredient.name)
        current_pizza_ingredient_quantity = lowest_quantity_ingredient.quantity_g
        recipe_ingredients.append(lowest_quantity_ingredient)
        if not any(ingredients):
            break

        lowest_i_category = lowest_quantity_ingredient.category
        lowest_i_name = lowest_quantity_ingredient.name
        # remove ingredient from categorized
        categorized_ingredients[lowest_i_category] = remove_ingredient_by_name(categorized_ingredients[lowest_i_category], lowest_i_name)
        for category, crt_ingredients in categorized_ingredients.items():
            if category == lowest_i_category:
                continue
            
            if not any(crt_ingredients):
                continue

            min_quantity = current_pizza_ingredient_quantity - (current_pizza_ingredient_quantity * RECIPE_QUANTITY_MARGIN)
            max_quantity = current_pizza_ingredient_quantity + (current_pizza_ingredient_quantity * RECIPE_QUANTITY_MARGIN)
            selected_i = pop_first_ingredient_in_range(crt_ingredients, min=min_quantity, max=max_quantity)

            # get max category quantity and move on
            if selected_i is None:
                max_i = max(crt_ingredients, key=lambda ingredient: ingredient.quantity_g)
                categorized_ingredients[category] = remove_ingredient_by_name(categorized_ingredients[category], max_i.name)
                selected_i = Ingredient(name = max_i.name, category=max_i.category, quantity_g=current_pizza_ingredient_quantity)
                leftover_i = Ingredient(name = max_i.name, category=max_i.category, quantity_g=(max_i.quantity_g - current_pizza_ingredient_quantity))
                categorized_ingredients[category].append(leftover_i)

            recipe_ingredients.append(selected_i)
        
        print(" ".join([f"{i.name}[{i.quantity_g}]" for i in recipe_ingredients]))
        # Step 4: Create the recipe
        recipe = Recipe(ingredients=recipe_ingredients)
        recipes.append(recipe)

    print(len(recipes))
    return recipes