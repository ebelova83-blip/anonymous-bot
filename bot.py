from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

TOKEN = "8887585380:AAEdehGlnB0slEWw_X_xZWm-MXI-nJtm_Kg"
OWNER_ID = 8595521730

async def forward_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
user = update.effective_user
text = update.message.text
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, forward_message))

print(“Бот запущен”)

app.run_polling()
