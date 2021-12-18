from aiogram import Bot, types
from aiogram.utils import executor
import yaml


config_path = "config.yml"


def get_token():
	with open(path, 'r') as config_file:
		config = yaml.load(config_file, Loader=yaml.BaseLoader)
	return config['tocken']



TOKEN = "ваш токен от бота здесь"
bot = Bot(token=TOKEN)
