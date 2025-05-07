from telegram import Update
from telegram.ext import ContextTypes
from bot.database import get_top_users

async def show_leaderboard(update: Update, context: ContextTypes.DEFAULT_TYPE):
    top = get_top_users()
    leaderboard = "\n".join([f"{u[0]}: {u[1]} coins" for u in top])
    await update.message.reply_text("🏆 Leaderboard:\n" + leaderboard)
