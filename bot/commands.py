import json
import logging
from typing import Union, Dict, List

from PyDictionary import PyDictionary
from telegram import Update
from telegram.ext import ContextTypes, CallbackContext

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE)-> None:
    """
    Initial command when the bot starts. It sends a greeting message with information on how to use the bot.

    :param update: Object that contains whichever updates are to be processed.
    :param context: Holds the context for the callback to be run in.
    """
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=("Hello, I'm a bot that's here to assist you in learning English!\n"
              "Please use the following commands:\n "
              "- <b>/mean </b>     <i>(add a word to get its meaning)</i>,\n"
              "- <b>/start_dialog</b>     <i>(to engage in a 'reading maze'</i>.\n"
              "You can also access our phrasal verb trainer by clicking the /menu_button.\n"
              "Best of luck!"),
        parse_mode='HTML'
    )

async def format_meaning(meaning: Union[str, Dict[str, List[str]]], word)-> str:
    """
    Formats the meaning of the word in a readable way.

    :param meaning: Meaning of the word.
    :param word: Word that the user asked the meaning of.
    :return: Formatted meaning.
    """
    formatted = f"<b>{word}:</b>\n"
    # Convert string to dictionary if it's not
    if isinstance(meaning, str):
        meaning = json.loads(meaning)
    # Iterate over each word type (e.g., Noun, Verb) in the dictionary
    for word_type, definitions in meaning.items():
        formatted += f"<i>({word_type})</i>:\n"
        # Iterate over each definition
        for i, definition in enumerate(definitions, 1):
            formatted += f"{i}. {definition}\n"
    return formatted

async def get_meaning(dictionary: PyDictionary, word: str)-> str:
    """
    Fetches the meaning of a word.

    :param dictionary: The dictionary from where the meanings are fetched.
    :param word: Word that the user asked the meaning of.
    :return: The meaning of the word or an error message.
    """
    try:
        meaning = dictionary.meaning(word)
        if meaning:
            return meaning
        else:
            return "Could not find a meaning for this word."
    except Exception as e:
        logging.error(f"Error getting meaning: {e}")
        return "An error occurred while trying to get the meaning."
    
async def meaning(update: Update, context: CallbackContext)-> None:
    """
    Sends the meaning of a word.

    :param update: Object that contains whichever updates are to be processed.
    :param context: Holds the context for the callback to be run in.
    """
    word = context.args[0]
    dictionary = context.bot_data['dictionary']
    raw_meaning = await get_meaning(dictionary, word)
    formatted_meaning = await format_meaning(raw_meaning, word)
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=formatted_meaning,
                                   parse_mode='HTML')
