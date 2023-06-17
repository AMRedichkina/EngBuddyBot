import logging
import json

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram.ext import filters, MessageHandler, CallbackContext

from PyDictionary import PyDictionary

from commands.meaning import get_meaning, format_meaning
from commands.synonym import get_synonym, format_synonym
from settings_env import BOT_TOKEN

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please give me a word!")

async def meaning(update: Update, context: CallbackContext):
    word = context.args[0]
    dictionary = context.bot_data['dictionary']
    raw_meaning = await get_meaning(dictionary, word)
    formatted_meaning = await format_meaning(raw_meaning, word)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=formatted_meaning, parse_mode='HTML')

async def synonym(update: Update, context: CallbackContext):
    word = context.args[0]
    raw_synonym = await get_synonym(word)
    formatted_synonim = await format_synonym(raw_synonym, word)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=formatted_synonim, parse_mode='HTML')

if __name__ == '__main__':
    application = ApplicationBuilder().token(BOT_TOKEN).build()
    dictionary = PyDictionary()

    # Store the dictionary in bot_data
    application.bot_data['dictionary'] = dictionary

    start_handler = CommandHandler('start', start)
    meaning_handler = CommandHandler('mean', meaning)
    synonym_handler = CommandHandler('synonym', synonym)
    
    application.add_handler(start_handler)
    application.add_handler(meaning_handler)
    application.add_handler(synonym_handler)
    
    application.run_polling()