from pyrogram import Client, filters
from config import API_ID, API_HASH, BOT_TOKEN, REACTION_AI
import random

app = Client(
    "ai_reaction_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

def get_ai_reaction(text):
    text = text.lower()
    for word, emojis in REACTION_AI.items():
        if word in text:
            return random.choice(emojis)
    return "👍"

@app.on_message(filters.group | filters.channel)
async def ai_react(client, message):
    try:
        if message.text or message.caption:
            content = message.text or message.caption
            reaction = get_ai_reaction(content)
            await client.send_reaction(
                chat_id=message.chat.id,
                message_id=message.id,
                emoji=reaction
            )
            print(f"Reacted: {reaction}")
    except Exception as e:
        print("Error:", e)

app.run()
