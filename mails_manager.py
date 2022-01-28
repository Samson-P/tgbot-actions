from aiogram import Bot
import yaml, time, asyncio
from get_mails import mail_manager


config_path = "/etc/tgbot-actions/config.yml"


def get_meta(cmd):
	with open(config_path, 'r') as config_file:
		config = yaml.load(config_file, Loader=yaml.BaseLoader)
	return config[cmd]


user = get_meta('user')
TOKEN = get_meta('token')


async def send_allert(message):
	alert_manager = Bot(token=TOKEN)
	await alert_manager.send_message(user, message)


def mail_checker():
	while True:
		response, err = mail_manager()
		ans = ''
		if err == None:
			[asyncio.run(send_allert(ans)) for ans in response]
		else:
			asyncio.run(send_allert(err))
		time.sleep(60)


if __name__ == '__main__':
	mail_checker()
