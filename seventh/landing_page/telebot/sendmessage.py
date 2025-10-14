import requests
from .models import TeleSettings


def send_telegram(tg_name, tg_phone):
    settings = TeleSettings.objects.get(pk=1)
    token = settings.tg_token
    chat_id = settings.tg_chat
    text = settings.tg_message
    api = 'https://api.telegram.org/bot'
    method = api + token + '/sendMessage'

    if text.find('{') and text.find('}') and text.rfind('{') and text.rfind('}'):
        part_1 = text[:text.find('{')]  # Заявка с сайта:\nИмя:
        part_2 = text[text.find('}') + 1:text.rfind('{')]  # \nТелефон:
        text_slice = part_1 + tg_name + part_2 + tg_phone
    else:
        text_slice = text

    requests.post(method, data={
        'chat_id': chat_id,
        'text': text_slice
    })
