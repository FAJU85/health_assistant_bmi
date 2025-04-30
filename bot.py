from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Define the /start command
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Welcome to the Health Assistant Bot! 🚀")

# Define a message handler for unrecognized commands
def handle_message(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("I didn't understand that. Try /start.")

# Main function to start the bot
def main():
    # Replace 'YOUR_TELEGRAM_TOKEN' with your bot token
    TOKEN = "Y7075930712:AAEwjnzFht21WtcsZA9nQBYnYZF5bwZ0L4s"
    updater = Updater(TOKEN)

    # Register the /start command
    updater.dispatcher.add_handler(CommandHandler("start", start))

    # Register a handler for all other messages
    updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()