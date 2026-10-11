import os
from groq import Groq


client = Groq(api_key=os.environ.get("GROQ_API_KEY"))


question = """
What is a merit scholarship?

Do not use any external tools or files.
Answer only from your own knowledge.
"""


response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {
            "role": "user",
            "content": question
        }
    ]
)


print("\n=== PLAIN LLM (NO TOOL) ===")

print("\nQuestion:")
print(question.strip())

print("\nAnswer:")
print(response.choices[0].message.content)