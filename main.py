from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from config import TELEGRAM_BOT_TOKEN
from database import add_user, get_credit

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    add_user(
        user.id,
        user.username if user.username else user.first_name
    )

    credit = get_credit(user.id)

    await update.message.reply_text(
        f"""🤖 DMPT AI BOT

Halo {user.first_name} 👋

💳 Kredit : {credit}

Bot berhasil online."""
    )

def main():
    app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("DMPT BOT ONLINE")

    app.run_polling()

if __name__ == "__main__":
    main()
