from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    user_name = update.message.from_user.first_name
    greetings = ["السلام", "السلام عليكم", "السلام عليكم ورحمة الله", "السلام عليكم ورحمة الله وبركاته"]
    
    if user_text in greetings:
        await update.message.reply_text(f"وعليكم السلام ورحمة الله وبركاته ياهلا فيك يا {user_name} 👋🏻")

if __name__ == '__main__':
    TOKEN = "8737393959:AAGfNXQAKc6SEemkh07KfBASY2SbIVv5Pek"
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), auto_reply))
    app.run_polling()
