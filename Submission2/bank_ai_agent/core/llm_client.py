
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

class LLMClient:
    def __init__(self):
        self.enabled = bool(os.getenv("OPENAI_API_KEY"))
        self.client = OpenAI() if self.enabled else None

    def generate(self, system_prompt, user_query, context=""):
        if not self.enabled:
            return f"[LLM disabled - set OPENAI_API_KEY]\nContext: {context}\nQuestion: {user_query}"

        response = self.client.chat.completions.create(
            model=os.getenv("OPENAI_MODEL","gpt-4o-mini"),
            messages=[
                {"role":"system","content":system_prompt},
                {"role":"user","content":f"Context:\n{context}\n\nQuestion:{user_query}"}
            ],
            temperature=0.2
        )
        return response.choices[0].message.content
