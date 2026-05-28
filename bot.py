from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

TOKEN = "TOKEN = "8887585380:AAEdehG1nB0slEWw_X_xZWm-MXI-nJtm_Kg"
OWNER_ID = 8595521730

async def forward_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    await context.bot.send_message(
        chat_id=OWNER_ID,
        text=f"📩 Новый анонимный вопрос:\n\n{text}"
    )

    await update.message.reply_text("Сообщение отправлено анонимно ✅")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, forward_message))

print("Бот запущен")
app.run_polling()
