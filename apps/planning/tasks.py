import json

import requests

from limon import settings
from limon.celery import app


def get_headers():
	return {
		"accept": "application/json",
		"content-type": "application/json"
	}


def get_text(data):
	return (
		f"""Клиент {data['name']} оставил заявку на часы {data['hours']}Номер телефона клиента: {data['phone']}"""
	)


@app.task
def ntfy_notify(data):

	ntfy_data = {
		"topic": "main",
		"message": get_text(data),
		"title": "Новая заявка на аренду",
		"tags": [
			"calendar",
		],
		"actions": [
			{
				"action": "view",
				"label": "Позвонить",
				"url": f"tel:{data['phone']}"
			}
		],
		"click": data['phone'],
		"priority": 4,
	}
	requests.post(
		'https://ntfy.tolq3.ru/',
		data=json.dumps(ntfy_data),
		auth=(settings.NTFY_USERNAME, settings.NTFY_PASSWORD)
	)


@app.task
def telegram_notify(data):
	message = {
		'chat_id': settings.CHAT_ID,
		'text': get_text(data)
	}

	try:
		requests.post(
			f'https://api.telegram.org/bot{settings.SYSTEM_NOTIFICATIONS_TELEGRAM_BOT_TOKEN}/sendMessage?parse_mode=HTML',
			data=json.dumps(message),
			timeout=500,
			headers=get_headers(),
		)
	except Exception as e:
		ntfy_data = {
			"topic": "main",
			"message": str(e),
			"title": "Ошибка отправки сообщения в телеграмм",
			"tags": [
				"facepalm",
			],
			"priority": 5,
		}
		requests.post(
			'https://ntfy.tolq3.ru/',
			data=json.dumps(ntfy_data),
			auth=(settings.NTFY_USERNAME, settings.NTFY_PASSWORD)
		)
