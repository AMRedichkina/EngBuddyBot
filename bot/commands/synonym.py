import logging
from wordhoard import Synonyms

async def format_synonym(synonyms, word):
    if synonyms == "Could not find a synonym for this word.":
        return "Could not find a synonym for this word."
    formatted = f"<b>{word}:</b>\n"
    length = len(synonyms)
    if length < 15:
        for i in synonyms:
            formatted += f'{i}, '
        return formatted
    else:
        for i in range(15):
            formatted += f'{synonyms[i]}, '
    return formatted

async def get_synonym(word):
    try:
        synonym = Synonyms(search_string=word)
        synonym_results = synonym.find_synonyms()
        if synonym_results:
            return synonym_results
        else:
            return "Could not find a synonym for this word."
    except Exception as e:
        logging.error(f"Error getting synonym: {e}")
        return "An error occurred while trying to get the synonym."