
import os   
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

def call_llm(prompt):
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.1,
        max_completion_tokens=128,
        stream=False
    )
    return completion.choices[0].message.content
