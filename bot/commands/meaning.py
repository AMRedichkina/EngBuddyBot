import logging
import json

async def format_meaning(meaning, word):
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

async def get_meaning(dictionary, word):
    try:
        meaning = dictionary.meaning(word)
        if meaning:
            return meaning
        else:
            return "Could not find a meaning for this word."
    except Exception as e:
        logging.error(f"Error getting meaning: {e}")
        return "An error occurred while trying to get the meaning."