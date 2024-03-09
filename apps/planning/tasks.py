import json

import requests

from limon import settings
from limon.celery import app


@app.task
def telegram_notify(data):
	text = (
		f'Клиент {data["name"]} оставил заявку на часы {data["hours"]}'
		f'Номер телефона клиента: <code>{data["phone"]}</code>'
	)

	headers = {
		"accept": "application/json",
		"content-type": "application/json"
	}
	message = {
				'chat_id': settings.CHAT_ID,
				'text': text
			}

	try:
		requests.post(
			f'https://api.telegram.org/bot{settings.SYSTEM_NOTIFICATIONS_TELEGRAM_BOT_TOKEN}/sendMessage?parse_mode=HTML',
			data=json.dumps(message),
			timeout=500,
			headers=headers,
		)
	except Exception as e:
		print(f'fuck {e}')