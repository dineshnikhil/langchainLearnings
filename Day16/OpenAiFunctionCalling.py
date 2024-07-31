# ==================== SETTING UP THE MODEL FROM OPEN AI ====================

import os
import json
from dotenv import load_dotenv
from langchain_openai import OpenAI
from openai import OpenAI

# ==================== LODING THE ENV VARIABLES =========================
load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

# ==================== INISIATING THE CLIENT =============================
client = OpenAI()

messages = [
    {"role": "user",
     "content": """What's the weather like in San Francisco,
                   New York, and Las Vegass?"""
    }
]

response = client.chat.completions.create(
    model="gpt-4o-mini-2024-07-18",
    messages=messages
)

print(response)