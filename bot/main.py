import logging

from telegram import __version__ as TG_VER

# Try importing telegram's version info. If not found, set it to zeros.
try:
    from telegram import __version_info__
except ImportError:
    __version_info__ = (0, 0, 0, 0, 0)

# Check telegram's version. If it is less than a certain version, raise a RuntimeError
if __version_info__ < (20, 0, 0, "alpha", 5):
    raise RuntimeError(
        f"This example is not compatible with your current PTB version {TG_VER}. To view the "
        f"{TG_VER} version of this example, "
        f"visit https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html"
    )

from telegram.ext import ApplicationBuilder, CommandHandler
from telegram.ext import filters, MessageHandler
from telegram.ext import ConversationHandler
from PyDictionary import PyDictionary

from commands import start, meaning
from dialog import start_dialog, cancel, answer
from dialog import answer2, answer3, answer4, answer5
from dialog import ANSWER, ANSWER2, LANGUAGE, ANSWER3, ANSWER4, ANSWER5
from settings_env import BOT_TOKEN

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

if __name__ == '__main__':
    # Build a new application
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    # Create an instance of PyDictionary
    dictionary = PyDictionary()

    # Store the dictionary in bot_data
    application.bot_data['dictionary'] = dictionary

    # Create handlers for /start and /mean commands
    start_handler = CommandHandler('start', start)
    meaning_handler = CommandHandler('mean', meaning)

    # Set up a conversation handler for multiple states of conversation
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start_dialog", start_dialog)],
        states={
            ANSWER: [MessageHandler(filters.Regex("^(Yes)$"), answer)],
            ANSWER2: [MessageHandler(filters.Regex("^(Yes|No)$"), answer2)],
            ANSWER3: [MessageHandler(filters.Regex("^(Yes|No|Accept|Reject|I would accept it|I would decline it)$"), answer3)],
            ANSWER4: [MessageHandler(filters.Regex("^(I would accept it|I would decline it|Accept|Reject|Stay|Go|Yes|No)$"), answer4)],
            ANSWER5: [MessageHandler(filters.Regex("^(Yes|No|ACCOUNTANT|PILOT|Stay|Go|Accept|Reject|I am excited|I am sad|AUSTRALIA|INDIA|Of course|Not exactly|I would accept it|I would decline it|Yes, I do|No, I don't)$"), answer5)],
            
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )

    # Add the handlers to the application
    application.add_handler(start_handler)
    application.add_handler(meaning_handler)
    application.add_handler(conv_handler)

    # Start the application by polling for updates
    application.run_polling()
    