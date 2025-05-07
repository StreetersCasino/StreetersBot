import requests
from telegram import Update
from telegram.ext import ContextTypes

async def get_price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Usage: /price <coin_name>")
        return
    coin = context.args[0].lower()
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    if coin in data:
        price = data[coin]["usd"]
        await update.message.reply_text(f"💸 {coin.capitalize()} price: ${price}")
    else:
        await update.message.reply_text("Coin not found.")
