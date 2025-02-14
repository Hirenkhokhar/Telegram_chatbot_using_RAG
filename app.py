import os
import telebot
from dotenv import load_dotenv
from chatbot import get_response

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    query = message.text
    response = get_response(query)
    bot.reply_to(message, response)

if __name__ == "__main__":
    bot.polling()
