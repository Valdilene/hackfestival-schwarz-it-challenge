from openai import OpenAI


def get_pizza_recipe_with_ingredients(ingredients: list[str], openai_client):
    completion = openai_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": f"What kind of pizza can you make with {', '.join(ingredients)}"
            }
        ]
    )
    return completion.choices[0].message.content
    
client = OpenAI()

with open("response.md", "w") as response_file:
    response_file.write(get_pizza_recipe_with_ingredients(["cheese", "chicken breast", "cherry tomatoes"], client))
