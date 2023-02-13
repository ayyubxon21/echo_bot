import telegram
import os


TOKEN = os.environ.get('TOKEN')
WEBHOOK='https://motof.pythonanywhere.com/api'
bot = telegram.Bot(token=TOKEN)

info=bot.getWebhookInfo()
# Delete the webhook
bot.deleteWebhook()
# Set the webhook
bot.setWebhook(WEBHOOK)
print(info)