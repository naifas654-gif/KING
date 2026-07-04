import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters
from aiohttp import web
import asyncio

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

async def handle(request):
    return web.Response(text="Bot is running!")

async def web_server():
    app = web.Application()
    app.router.add_get('/', handle)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', int(os.environ.get('PORT', 10000)))
    await site.start()

async def handle_greetings(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    greetings = ["سلام", "السلام عليكم", "السلام عليكم ورحمة الله", "السلام عليكم ورحمة الله وبركاته"]
    
    if any(g == user_text.strip() for g in greetings):
        user_name = update.effective_user.first_name
        reply = f"وعليكم السلام ورحمة الله وبركاته، ياهلا فيك يا {user_name} 👋🏻"
        await update.message.reply_text(reply)

if __name__ == '__main__':
    TOKEN = "8737393959:AAGfNXQAKc6SEemkh07KfBASY2SbIVv5Pek"
    
    asyncio.get_event_loop().run_until_complete(web_server())
    
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_greetings))
    app.run_polling()
