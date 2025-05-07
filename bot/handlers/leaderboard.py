# bot/handlers/leaderboard.py

from telegram import Update
from telegram.ext import ContextTypes

async def leaderboard_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Temporary static leaderboard
    leaderboard_text = (
        "🏆 Leaderboard:\n"
        "1. Alice - 150 coins\n"
        "2. Bob - 120 coins\n"
        "3. Charlie - 100 coins"
    )
    await update.message.reply_text(leaderboard_text)
