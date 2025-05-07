from telegram import Update
from telegram.ext import ContextTypes
from bot.database import register_user, user_exists

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    if user_exists(user.id):
        await update.message.reply_text("You're already registered.")
    else:
        await update.message.reply_text("Welcome! Use /register <email> <wallet> to sign up.")

async def register(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) != 2:
        await update.message.reply_text("Usage: /register <email> <wallet_address>")
        return
    email, wallet = context.args
    register_user(update.effective_user, email, wallet)
    await update.message.reply_text("Registration successful! 🎉")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(update.message.text)
