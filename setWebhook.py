import requests
import os


TOKEN = os.environ.get('TOKEN')
url='https://ayyubxon679.pythonanywhere.com/api'
TOKEN=os.environ['TOKEN']

payload = {
    "url": url
}
response = requests.get(f'https://api.telegram.org/bot{TOKEN}/setWebhook', params=payload)
print(response.status_code)