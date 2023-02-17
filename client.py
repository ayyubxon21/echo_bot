from telegram.ext import CallbackContext
from telegram import Bot, Update

def start(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    bot=context.bot

    bot.send_message(chat_id=chat_id, text='Hello World!')

def echo(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    text = update.message.text
    bot=context.bot

    bot.sendMessage(chat_id=chat_id, text=text)

def shop(update: Update, context: CallbackContext):
    chat_id=update.message.chat_id
    bot=context.bot
    bot.send_message(chat_id=chat_id, text='Welcome')