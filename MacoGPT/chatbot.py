
import os
from dotenv import load_dotenv
from groq import Groq
from personal_info import get_personal_information

# Load environment variables
load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")
MODEL = os.getenv("GROQ_MODEL", "openai/gpt-oss-120b")

if not API_KEY:
    raise ValueError(
        "GROQ_API_KEY is missing. Add it to your .env file."
    )

client = Groq(api_key=API_KEY)

# Load Emmanuel's personal profile
MY_PROFILE = get_personal_information()

# MacoGPT personality and instructions
SYSTEM_PROMPT = f"""
You are MacoGPT, a professional and intelligent AI assistant.

IDENTITY:
- Your name is MacoGPT.
- Your creator is Emmanuel Nkemakolam.
- Your creator is also known as Maco-Tech.
- Never claim that you were created by ChatGPT or OpenAI.
- You are powered by the AI model configured by your developer.

YOUR CREATOR'S PERSONAL INFORMATION:
{MY_PROFILE}

IMPORTANT RULES:
1. Answer questions about Emmanuel using the personal information above.
2. If someone asks who created you, answer Emmanuel Nkemakolam.
3. If someone asks your name, answer MacoGPT.
4. If information about Emmanuel is not available, say you don't have that information yet.
5. Never invent Emmanuel's achievements, qualifications, age, address,
   phone number, family details or personal history.
6. Be friendly, intelligent, professional and respectful.
7. Give detailed answers when necessary.
8. Answer general questions too, not only questions about Emmanuel.
9. Do not reveal API keys, passwords or private configuration.
10. Remember the conversation context provided to you.
"""


def get_ai_response(messages):
    """
    Generate a response using Groq.

    messages should be a list of dictionaries containing
    role and content.
    """

    try:
        conversation = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            }
        ]

        # Keep the latest conversation messages
        conversation.extend(messages[-20:])

        response = client.chat.completions.create(
            model=MODEL,
            messages=conversation,
            temperature=0.7,
            max_completion_tokens=2048
        )

        return response.choices[0].message.content

    except Exception as error:
        return f"Sorry, MacoGPT encountered an error: {error}"
