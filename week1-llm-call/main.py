
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

print("Program Started!")

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Gemini API key not found!")

print("Gemini API Key Loaded Successfully!")

client = genai.Client(api_key=api_key)

print("Connecting to Gemini...")

response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents="""
    Explain clustering in AI.
    Include its meaning and two real-world applications.
    Use simple language and bullet points.
    """,
    config=types.GenerateContentConfig(
        temperature=0.7,
        max_output_tokens=300
    )
)

print("\n========== LLM RESPONSE ==========")
print(response.text)
print("==================================")
