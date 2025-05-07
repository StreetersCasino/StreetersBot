from telegram import Update
from telegram.ext import ContextTypes

# Import handlers
from bot.handlers.leaderboard import leaderboard_command
from bot.crypto import get_price
from bot.handlers.game_dice import play_dice  # ✅ Import this

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Welcome to the Telegram bot! 🍡\nUse /help to see available commands."
    )

# /help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Here are the available commands:\n"
        "/start - Welcome message\n"
        "/help - Show this help message\n"
        "/leaderboard - View the top players\n"
        "/price <coin> - Get the current price of a coin\n"
        "/play_dice <1-12> - Guess a dice roll to win coins"
    )

# Setup command handlers
def setup_handlers(application):
    from telegram.ext import CommandHandler

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("leaderboard", leaderboard_command))
    application.add_handler(CommandHandler("price", get_price))
    application.add_handler(CommandHandler("play_dice", play_dice))  # ✅ Add this
