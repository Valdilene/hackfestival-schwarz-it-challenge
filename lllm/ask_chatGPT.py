from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "What kind of pizza can you make with porc and zuchinni?"
        }
    ]
)

with open("response.md", "w") as response_file:
    response_file.write(completion.choices[0].message.content)