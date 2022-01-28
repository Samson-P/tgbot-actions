from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import yaml, time, asyncio
from get_mails import mail_manager
from threading import Thread



config_path = "/etc/tgbot-actions/config.yml"
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


user = get_meta('user')
TOKEN = get_meta('token')
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
	keyboard = types.ReplyKeyboardMarkup()
	button = types.KeyboardButton(text="Проверить почту")
	bottom = ["О нас", "Приветствие"]
	keyboard.add(button)
	keyboard.add(*bottom)
	await message.answer(messages['start'], reply_markup=keyboard)


@dp.message_handler(commands="hello")
async def cmd_start(message: types.Message):
	await message.answer(messages['hello'].format(repo))


@dp.message_handler(content_types=['text'])
async def get_text_messages(msg: types.Message):
	if msg.text.lower() == 'привет' or msg.text.lower() == 'приветствие':
		await msg.answer(messages['hello'].format(repo))
	elif msg.text.lower() == '/show' or msg.text.lower() == "проверить почту":
		response, err = mail_manager()
		ans = ''
		if err == None:
			[await msg.answer(ans) for ans in response]
		else:
			await msg.answer(err)
	elif msg.text.lower() == '/info' or msg.text.lower() == "о нас":
		await msg.answer(messages['info'].format(last_release))
	else:
		await msg.answer('Не понимаю, что это значит.')


if __name__ == '__main__':
	executor.start_polling(dp)
