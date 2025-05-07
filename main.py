import os
from contextlib import asynccontextmanager
from http import HTTPStatus
from dotenv import load_dotenv
from fastapi import FastAPI, Request, Response
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

from bot.commands import setup_handlers

# Load environment variables
load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
WEBHOOK_DOMAIN = os.getenv("RAILWAY_PUBLIC_DOMAIN")

bot_app = Application.builder().token(TELEGRAM_BOT_TOKEN).updater(None).build()
setup_handlers(bot_app)

@asynccontextmanager
async def lifespan(_: FastAPI):
    await bot_app.bot.setWebhook(url=WEBHOOK_DOMAIN)
    async with bot_app:
        await bot_app.start()
        yield
        await bot_app.stop()

app = FastAPI(lifespan=lifespan)

@app.post("/")
async def process_update(request: Request):
    data = await request.json()
    update = Update.de_json(data=data, bot=bot_app.bot)
    await bot_app.process_update(update)
    return Response(status_code=HTTPStatus.OK)
