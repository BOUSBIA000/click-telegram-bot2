
📌 خطوات رفع البوت على Render:

1. ارفع الملفات إلى GitHub (أو مباشرة إلى Render).
2. ادخل https://render.com وسجل دخولك.
3. اختر "New Web Service".
4. اربط المستودع، ثم استخدم الإعدادات التالية:
   - Build Command: pip install -r requirements.txt
   - Start Command: python main.py

5. أضف متغيرات البيئة (Environment Variables):
   - BOT_TOKEN = توكن البوت من BotFather
   - WEBHOOK_URL = رابط Render بعد أول نشر (مثال: https://yourbot.onrender.com)

6. بعد أول تشغيل، انسخ رابط الموقع وأضفه في WEBHOOK_URL وأعد النشر.

🔁 البوت يستخدم Webhook، ويعمل بشكل تلقائي على Render.
