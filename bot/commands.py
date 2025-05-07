from telegram import Update
from telegram.ext import ContextTypes

# --- Basic Commands ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Welcome to the Telegram bot! 🍡\nUse /help to see available commands."
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Available commands:\n"
        "/start - Welcome message\n"
        "/help - Show this help message\n"
        "/leaderboard - View the top players\n"
        "/price [coin] - Get the current price of a coin (e.g., /price bitcoin)\n"
        "/dice - Play a dice game\n"
        "/blackjack - Play a blackjack game\n"
        "/register - Register your email and wallet"
    )

# --- Import handlers from their modules ---
from bot.handlers.leaderboard import leaderboard_command
from bot.handlers.game_dice import dice_command
from bot.handlers.game_blackjack import blackjack_command
from bot.handlers.user_info import register_command
from bot.crypto import price_command

# --- Register Handlers ---
def setup_handlers(application):
    from telegram.ext import CommandHandler

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("leaderboard", leaderboard_command))
    application.add_handler(CommandHandler("price", price_command))
    application.add_handler(CommandHandler("dice", dice_command))
    application.add_handler(CommandHandler("blackjack", blackjack_command))
    application.add_handler(CommandHandler("register", register_command))
