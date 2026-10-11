from config import client, MODEL

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "user", "content": user_input}
        ],
        temperature=0.7,
    )

    print("Bot:", response.choices[0].message.content)
    