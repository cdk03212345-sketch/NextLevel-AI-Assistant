import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def ask_ai(message):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": """
You are NextLevel Personal AI Assistant.

You help your owner with:
- Business tasks
- Websites
- Bots
- Daily work

Reply in Bangla.
Be helpful and concise.
"""
            },
            {
                "role": "user",
                "content": message
            }
        ]
    )

    return response.choices[0].message.content
