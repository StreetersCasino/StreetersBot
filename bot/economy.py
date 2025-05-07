from bot.database import update_balance, get_balance_for_user

def add_coins(user_id, amount):
    update_balance(user_id, amount)

def remove_coins(user_id, amount):
    update_balance(user_id, -amount)

def get_balance(user_id):
    return get_balance_for_user(user_id)

async def show_balance(update, context):
    balance = get_balance(update.effective_user.id)
    await update.message.reply_text(f"💰 You have {balance} coins.")
