
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "7802908032:AAFH89zGnDWhrOKJleyQ3HDC8dkCzLWaWOc"

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("✅ Receber sinais", callback_data='sinais')],
        [InlineKeyboardButton("🔓 Entrar no grupo VIP", url='https://t.me/seulinkdogrupo')],
        [InlineKeyboardButton("💬 Falar com o suporte", url='https://t.me/seusuporteaqui')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "👋 Bem-vindo ao *ApostaJá Bot!*
Receba sinais gratuitos de apostas esportivas direto no Telegram!",
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "sinais":
        await query.edit_message_text(text="🎯 Aqui vão os sinais de hoje:\n\n- Flamengo x Palmeiras: +2.5 gols\n- Barcelona x Real Madrid: Ambas marcam")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    app.run_polling()

if __name__ == "__main__":
    main()
