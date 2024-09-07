import requests

from process_data import process_foods
from upcycle_recipes import Ingredient, PizzaIngredientCategory

# Function to convert weight to grams
def convert_to_grams(weight: str) -> float:
    if "kg" in weight:
        return float(weight.replace("kg", "")) * 1000
    elif "g" in weight:
        return float(weight.replace("g", ""))
    else:
        raise ValueError(f"Unknown weight unit: {weight}")


# Function to fetch data and transform it into a list of Ingredients
def fetch_ingredients_from_url(url: str) -> list[Ingredient]:
    response = requests.get(url)
    response.raise_for_status()  # Raises an error for bad responses

    # Parse the response JSON
    items = response.json()["items"]

    ingredients = []
    for item in items:
        name = item['name']
        available_units = item['available']
        try:
            weight_per_unit = convert_to_grams(item['weight'])
        except ValueError as e:
            print(e)
            continue

        # Calculate total quantity in grams
        total_quantity = available_units * weight_per_unit
        
        # Assuming the ingredient belongs to the Veggie category
        ingredient = Ingredient(name=name, quantity_g=total_quantity)
        
        ingredients.append(ingredient)

        requests.delete(f"http://127.0.0.1:8000/backend/api/items/{item['id']}")
    return ingredients


# Example usage:
url = "http://127.0.0.1:8000/backend/api/items/"  # Replace with the actual URL
ingredients = fetch_ingredients_from_url(url)

process_foods(ingredients=ingredients)