from telegram import Update
from telegram.ext import ContextTypes
from bot.economy import add_coins, remove_coins, get_balance

# Placeholder blackjack logic
async def play_blackjack(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if get_balance(user_id) < 1:
        await update.message.reply_text("You need at least 1 coin to play.")
        return
    import random
    win = random.choice([True, False])
    if win:
        add_coins(user_id, 2)
        await update.message.reply_text("You won at blackjack! 🎲 (+2 coins)")
    else:
        remove_coins(user_id, 1)
        await update.message.reply_text("You lost at blackjack. (-1 coin)")
