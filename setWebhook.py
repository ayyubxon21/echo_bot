import requests
import os


url='https://ayyubxon679.pythonanywhere.com/webhook'
TOKEN=os.environ['TOKEN']

payload = {
    "url": url
}
response = requests.get(f'https://api.telegram.org/bot{TOKEN}/setWebhook', params=payload)
print(response.status_code)