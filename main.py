import time
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "COLOQUE_SEU_TOKEN_AQUI"

LINK_AFILIADO = "https://br4.bet.br/?ref=466167&btag=lvcyeqrnmzzkwhgszrziafxufc&login=0&campaign_id=17170"

LINK_COMPARTILHAR = "https://t.me/share/url?url=https://t.me/+TWaiGZqe1iM5NDE5&text=Venha para o grupo VIP!"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    msg1 = (
        "🔥 *BEM-VINDO!* 🔥\n\n"
        "Antes de tudo, crie sua conta na plataforma oficial:\n\n"
        "👇 *Clique no botão abaixo* 👇"
    )

    botoes1 = [
        [InlineKeyboardButton("💰 Criar Conta", url=LINK_AFILIADO)]
    ]

    await update.message.reply_text(
        msg1,
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(botoes1)
    )

    time.sleep(10)

    msg2 = (
        "📣 *Compartilhe com seus amigos!*\n"
        "Convide outras pessoas para entrar no grupo:"
    )

    botoes2 = [
        [InlineKeyboardButton("📤 Compartilhar", url=LINK_COMPARTILHAR)]
    ]

    await update.message.reply_text(
        msg2,
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(botoes2)
    )


def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot rodando no Render…")
    app.run_polling()


if __name__ == "__main__":
    main()
