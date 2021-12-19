from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import yaml
from get_mails import mail_manager


config_path = "config.yml"

repo = "Samson-P/tgbot-actions"
last_release = "20.12.2021 00:03"
messages = {
	'hello': "Привет! Я могу предоставить тебе информацию о последней сборке GitHub репозитория {}",
	'info': "Посдений релиз был {}",
	'start': """Приветствую, чем могу помочь? 
		/start
		/info
		/hello
		/show
	""",

}


def get_meta(cmd):
	with open(config_path, 'r') as config_file:
		config = yaml.load(config_file, Loader=yaml.BaseLoader)
	return config[cmd]


TOKEN = get_meta('tocken')
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(content_types=['text'])
async def get_text_messages(msg: types.Message):
	if msg.text.lower() == 'привет' or msg.text.lower() == '/hello':
		await msg.answer(messages['hello'].format(repo))
	elif msg.text.lower() == '/show':
		response, err = mail_manager()
		ans = ''
		if err == None:
			[await msg.answer(ans) for ans in response]
		else:
			await msg.answer(err)
	elif msg.text.lower() == '/info':
		await msg.answer(messages['info'].format(last_release))
	elif msg.text.lower() == '/start':
		await msg.answer(messages['start'])
	else:
		await msg.answer('Не понимаю, что это значит.')


if __name__ == '__main__':
   executor.start_polling(dp)
