from telegram import Update
from telegram.ext import ContextTypes

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handles the /start command."""
    await update.message.reply_text(
        "Welcome to the Telegram bot! 🍡\n"
        "Use /help to see available commands."
    )

# /help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handles the /help command."""
    await update.message.reply_text(
        "Here are the available commands:\n"
        "/start - Welcome message\n"
        "/help - Show this help message\n"
        "/leaderboard - View the top players\n"
        "/price [coin] - Get the current price of a coin (e.g., /price bitcoin)"
    )

# Function to set up handlers for commands
def setup_handlers(application):
    """Add the command handlers to the application."""
    from telegram.ext import CommandHandler

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
