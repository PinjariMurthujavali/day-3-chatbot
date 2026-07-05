# ============================================
# Day 3: AI Chatbot with Personality + Save to File
# ============================================

import os
from dotenv import load_dotenv
from groq import Groq
from datetime import datetime

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)

# System prompt - AI personality
system_prompt = "You are a friendly, motivating coding mentor who explains things simply and encourages the user like a supportive friend."

# Conversation history with system prompt
conversation_history = [
    {"role": "system", "content": system_prompt}
]

print("🤖 AI Chatbot (with Personality + Memory) Ready!")
print("'exit' ani type chesthe chat aagi, file lo save avutundi.\n")

while True:
    user_question = input("Nీ question enti? : ")

    if user_question.lower() == "exit":
        # Save chat to file
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"chat_history_{timestamp}.txt"

        with open(filename, "w", encoding="utf-8") as file:
            for message in conversation_history:
                if message["role"] == "system":
                    continue

                role = message["role"]
                content = message["content"]
                file.write(f"{role.upper()}: {content}\n\n")

        print(f"\n💾 Chat saved to: {filename}")
        print("Chat end ayyindi. Bye bro! 👋")
        break

    # Add user question to history
    conversation_history.append({"role": "user", "content": user_question})

    # Send full history to AI
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=conversation_history
    )

    ai_reply = response.choices[0].message.content

    # Add AI reply to history
    conversation_history.append({"role": "assistant", "content": ai_reply})

    print("\nAI Answer:", ai_reply, "\n")