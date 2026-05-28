from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

TOKEN = “СЮДА_ВСТАВЬ_ТОКЕН_ОТ_BOTFATHER”
OWNER_ID = СЮДА_ВСТАВЬ_ТВОЙ_TELEGRAM_ID

async def forward_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
user = update.effective_user
text = update.message.text
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, forward_message))

print(“Бот запущен”)

app.run_polling()