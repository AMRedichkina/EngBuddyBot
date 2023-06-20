from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ContextTypes
from telegram.ext import ConversationHandler

ANSWER, ANSWER2, ANSWER3, ANSWER4, ANSWER5 = range(5)

async def start_dialog(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """
    Sends the initial greeting to the user and sets up the game.

    :param update: An object that contains all the incoming update data.
    :param context: A context object containing information for the callback function.
    :return: The next state for the conversation.
    """
    reply_keyboard = [["Yes"]]
    await update.message.reply_photo("./images/JJ.png")
    await update.message.reply_text(
        "Welcome to the journey of Jolly Jumper's life! "
        "In this game, you'll guide Jolly through a labyrinth of life choices. "
        "As your bot assistant, I will pose various questions, and you will make "
        "decisions that determine the course of Jolly's life.\n"
        "<b>Reflect upon each question and attempt to construct sentences "
        "about the impact each choice may have.</b>\n"
        "Consider the scenarios that would or wouldn't have unfolded if Jolly had made certain decisions differently.\n" 
        "<b>For example:</b>\n"
        "- If Jolly hadn't gone to university, he wouldn't have ended up working in France.\n"
        "- If Jolly had taken that promotion, he would now be working in London.\n"
        "Now, fasten your seatbelt for this exciting journey through Jolly Jumper's life. Let's begin!\n\n"
        "Send /cancel to stop talking to me.\n\n"
        "If you want to continue send 'Yes'?",
        parse_mode='HTML',
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="Yes or No?"
        ),
    )
    return ANSWER

async def answer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """
    Handles the first question of the game.

    :param update: An object that contains all the incoming update data.
    :param context: A context object containing information for the callback function.
    :return: The next state for the conversation.
    """
    reply_keyboard = [["Yes", "No"]]
    await update.message.reply_text(
        "You have an offer of a place at university. Do you take it?",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="Do you take it?"
        ),
    )
    return ANSWER2

async def answer2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """
    Handles the second question of the game.

    :param update: An object that contains all the incoming update data.
    :param context: A context object containing information for the callback function.
    :return: The next state for the conversation.
    """
    user_response = update.message.text
    if user_response == 'Yes':
        reply_keyboard = [["JAPANESE"], ["FRENCH"]]
        await update.message.reply_text(
            "You decide to study a language: Japanese or French. Which one do you choose?",
            reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="Which one do you choose?"
            ),
        )
        return ANSWER3
    else:
        reply_keyboard = [["Yes", "No"]]
        await update.message.reply_text(
            "You secure a job in an office and are offered a promotion. Do you accept?",
            reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="Do you accept?"
            ),
        )
        return ANSWER3

async def answer3(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """
    Handles the third question of the game.

    :param update: An object that contains all the incoming update data.
    :param context: A context object containing information for the callback function.
    :return: The next state for the conversation.
    """
    user_response = update.message.text
    if user_response == 'Yes':
        reply_keyboard = [["Yes"], ["No"]]
        await update.message.reply_text(
            "They want you to move to London. Do you go?",
            reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="Do you go?"
            ),
        )
        return ANSWER4

    elif user_response == 'No':
        reply_keyboard = [["Stay", "Go"]]
        await update.message.reply_text(
            "You find that you don't enjoy your job. Do you choose to stay or leave?",
            reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="Do you stay or go?"
            ),
        )
        return ANSWER4

    elif user_response == 'JAPANESE':
        reply_keyboard = [["Accept", "Reject"]]
        await update.message.reply_text(
            "You have the offer of a job in Japan. Do you accept it?",
            reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="Do you accept it?"
            ),
        )
        return ANSWER4

    elif user_response == 'FRENCH':
        reply_keyboard = [["I would accept it", "I would decline it"]]
        await update.message.reply_text(
            "You have the offer of a job in France."
            "What would you do if you received a job offer from France?",
            reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="Do you accept it?"
            ),
        )
        return ANSWER4

async def answer4(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """
    Handles the forth question of the game.

    :param update: An object that contains all the incoming update data.
    :param context: A context object containing information for the callback function.
    :return: The next state for the conversation.
    """
    user_response = update.message.text
    if user_response == 'Yes' or user_response == 'Accept' or user_response == 'I would accept it':
        reply_keyboard = [["Yes"], ["No"]]
        await update.message.reply_text(
            "You meet someone who wants to marry you. Do you accept?",
            reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="Do you accept?"
            ),
        )
        return ANSWER5

    elif user_response == 'No':
        reply_keyboard = [["ACCOUNTANT"], ["PILOT"]]
        await update.message.reply_text(
            "You decide to retrain for a new career: accountant or pilot. Which do you choose?",
            reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="Which do you choose?"
            ),
        )
        return ANSWER5

    elif user_response == 'Stay':
        reply_keyboard = [["I am excited", "I am sad"]]
        await update.message.reply_text(
            "You get relocated to the New York office. How do you feel about this?",
            reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="How do you feel about this?"
            ),
        )
        return ANSWER5

    elif user_response == 'Go':
        reply_keyboard = [["AUSTRALIA", "INDIA"]]
        await update.message.reply_text(
            "You decide to embark on a round-the-world journey. Where do you head to first?",
            reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="Where do you go first?"
            ),
        )
        return ANSWER5

    elif user_response == 'Reject':
        reply_keyboard = [["Of course", "Not exactly"]]
        await update.message.reply_text(
            "You're teaching Japanese in the UK. Are you enjoying it?",
            reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="Do you like it?"
            ),
        )
        return ANSWER5

    elif user_response == 'I would decline it':
        reply_keyboard = [["Yes, I do", "No, I don't"]]
        await update.message.reply_text(
            "You come across an ad offering cabin crew training for Air France. Would you apply?",
            reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="Do you apply?"
            ),
        )
        return ANSWER5

async def answer5(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """
    Handles the fifth question of the game.

    :param update: An object that contains all the incoming update data.
    :param context: A context object containing information for the callback function.
    :return: The next state for the conversation.
    """
    user_response = update.message.text
    if user_response == 'Yes':
        await update.message.reply_text(
            "You get married and stay in the city. You are happy \U0001F600"
            )
        return ConversationHandler.END
    
    elif user_response == 'No':
        await update.message.reply_text(
            "All doors are open, you are building a dizzying career."
            )
        return ConversationHandler.END
    
    elif user_response == 'ACCOUNTANT':
        await update.message.reply_text(
            "You work in London and become very rich."
            )
        return ConversationHandler.END
    elif user_response == 'PILOT':
        await update.message.reply_text(
            "You travel all over the world."
        )
        return ConversationHandler.END
    elif user_response == 'I am excited':
        await update.message.reply_text(
            "You stay in the US"
        )
        return ConversationHandler.END
    elif user_response == 'I am sad':
        await update.message.reply_text(
            "You move to New Zealand."
        )
        return ConversationHandler.END
    elif user_response == 'AUSTRALIA':
        await update.message.reply_text(
            "You meet someone, settle down and stay in Australia"
        )
        return ConversationHandler.END
    elif user_response == 'INDIA':
        await update.message.reply_text(
            "You end up working for a charity in India."
        )
        return ConversationHandler.END
    
    elif user_response == 'Of course':
        await update.message.reply_text(
            "You start your own school."
        )
        return ConversationHandler.END
    
    elif user_response == 'Not exactly':
        await update.message.reply_text(
            "You become a UN interpreter"
        )
        return ConversationHandler.END
    
    elif user_response == 'Yes, I do':
        await update.message.reply_text(
            "You become a steward(ess) and travel all over the world."
        )
        return ConversationHandler.END

    elif user_response == "No, I don't":
        await update.message.reply_text(
            "You take a job as a translator."
        )
        return ConversationHandler.END


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """
    Ends the conversation when the user sends /cancel.

    :param update: An object that contains all the incoming update data.
    :param context: A context object containing information for the callback function.
    :return: The next state for the conversation, which is ConversationHandler.END in this case.
    """
    user = update.message.from_user
    await update.message.reply_text(
        "Bye! I hope we can talk again some day.", reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END
