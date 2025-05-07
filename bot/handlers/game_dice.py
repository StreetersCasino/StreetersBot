import random
from telegram import Update
from telegram.ext import ContextTypes
from bot.economy import add_coins, get_balance

async def play_dice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message is None:
        return  # Ignore updates without a message (e.g., button clicks, joins)

    if len(context.args) != 1 or not context.args[0].isdigit():
        await update.message.reply_text("Usage: /play_dice <number 1-12>")
        return

    guess = int(context.args[0])
    if not 1 <= guess <= 12:
        await update.message.reply_text("Choose a number between 1 and 12.")
        return

    roll = random.randint(1, 6) + random.randint(1, 6)
    if guess == roll:
        add_coins(update.effective_user.id, 1)
        await update.message.reply_text(f"You guessed right! 🎉 The roll was {roll}. You won 1 coin.")
    else:
        await update.message.reply_text(f"No luck! The roll was {roll}.")
