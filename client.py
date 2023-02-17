from telegram.ext import CallbackContext
from telegram import Bot, Update, InlineKeyboardButton, InlineKeyboardMarkup

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
    iphone = InlineKeyboardButton(text='Iphone',callback_data='phone_list Apple')
    samsung = InlineKeyboardButton(text='Samsung',callback_data='phone_list Samsung')
    huawei = InlineKeyboardButton(text='Huawei',callback_data='phone_list Huawei')
    xiaomi = InlineKeyboardButton(text='Redmi',callback_data='phone_list Redmi')
    vivo = InlineKeyboardButton(text='Vivo',callback_data='phone_list Vivo')
    oppo = InlineKeyboardButton(text='Oppo',callback_data='phone_list Oppo')
    

    # Define keyboard
    keyboar = InlineKeyboardMarkup([
        [iphone,samsung,huawei],
        [xiaomi,vivo,oppo]
    ])

    bot = context.bot
    bot.sendMessage(chat_id=chat_id,text='Choose a phone',reply_markup=keyboar)