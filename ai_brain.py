import json
import os
from datetime import datetime

MEMORY_FILE = "memory.json"


def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)

    return {
        "name": "",
        "notes": []
    }


def save_memory(data):
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def ask_ai(message):

    memory = load_memory()

    msg = message.lower()


    # Save name
    if "my name is" in msg:
        name = message.replace("my name is", "").strip()
        memory["name"] = name
        save_memory(memory)

        return f"ঠিক আছে, আমি মনে রাখলাম আপনার নাম {name}"


    # Remember
    if "remember" in msg:
        note = message.replace("remember", "").strip()

        memory["notes"].append({
            "text": note,
            "date": str(datetime.now())
        })

        save_memory(memory)

        return "ঠিক আছে, আমি এটা মনে রাখলাম।"


    # Show memory
    if "what do you remember" in msg:
        return str(memory)


    # Basic commands

    if "hello" in msg or "hi" in msg:
        return "হ্যালো 👋 আমি NextLevel AI Assistant."


    if "who are you" in msg:
        return "আমি NextLevel Personal AI Assistant."


    if "time" in msg:
        return datetime.now().strftime("%I:%M %p")


    return """
আমি বুঝতে পারছি না এখনো।
আপনি আমাকে নতুন command শেখাতে পারবেন।
ভবিষ্যতে আমি website, bot এবং device control করতে পারবো।
"""
