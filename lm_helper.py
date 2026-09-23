
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.7,
    groq_api_key=os.getenv("GROQ_API_KEY")
)

def generate_post(topic, tone, length):
    prompt = f"""
    You are a professional LinkedIn post writer.

    Write a LinkedIn post about: {topic}
    Tone: {tone}
    Length: {length}

    Guidelines:
    - Start with an engaging hook.
    - Use short, readable paragraphs.
    - Make it natural and engaging.
    - Add relevant hashtags.
    - Return only the post.
    """

    response = llm.invoke(prompt)
    return response.content