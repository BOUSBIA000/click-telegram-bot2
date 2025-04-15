
import os
from flask import Flask, request
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8086056766:AAHts4apA7AUx4MatyTQfQnCLoYBOgWvHdA"
URL = os.getenv("https://click-telegram-bot.onrender.com/")  # رابط الدومين من Render

user_data = {}

app = Flask(__name__)

telegram_app = Application.builder().token(TOKEN).build()

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uid = update.effective_user.id
    if uid not in user_data:
        user_data[uid] = {"coins": 0}

    keyboard = [[InlineKeyboardButton("🖱️ انقر", callback_data="click")]]
    markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        f"""أهلًا {update.effective_user.first_name}!
💰 رصيدك: {user_data[uid]['coins']}""",
        reply_markup=markup
    )

# الضغط
async def click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    uid = query.from_user.id
    user_data[uid]["coins"] += 1

    await query.answer()
    await query.edit_message_text(
        text=f"""🖱️ نقرت!
💰 رصيدك: {user_data[uid]['coins']}""",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🖱️ انقر", callback_data="click")]])
    )

telegram_app.add_handler(CommandHandler("start", start))
telegram_app.add_handler(CallbackQueryHandler(click, pattern="click"))

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(), telegram_app.bot)
    telegram_app.update_queue.put_nowait(update)
    return "OK"

@app.route("/")
def home():
    return "بوتك شغال 💪"

if __name__ == "__main__":
    telegram_app.run_webhook(
        listen="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        webhook_url=f"{URL}/{TOKEN}"
    )
