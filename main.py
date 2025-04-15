import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

# === إعداد التوكن ورابط السيرفر ===
TOKEN = "8086056766:AAHts4apA7AUx4MatyTQfQnCLoYBOgWvHdA"
WEBHOOK_PATH = f"/{TOKEN}"
WEBHOOK_URL = f"https://click-telegram-bot.onrender.com{WEBHOOK_PATH}"  # رابط المشروع على Render

# === إعداد السجل ===
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# === الأوامر ===
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"أهلًا {update.effective_user.first_name}! 👋\nمرحبًا بك في لعبة BAHI BOTS ⚙️")

async def click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ نقرتك تم تسجيلها!")

# === تشغيل التطبيق ===
async def main():
    app = ApplicationBuilder().token(TOKEN).build()

    # أوامر البوت
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("click", click))

    # تسجيل Webhook
    await app.bot.set_webhook(url=WEBHOOK_URL)

    # تشغيل الخادم
    await app.run_webhook(
        listen="0.0.0.0",
        port=int(os.environ.get("PORT", 10000)),
        webhook_path=WEBHOOK_PATH,
        allowed_updates=Update.ALL_TYPES,
    )

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
