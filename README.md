# tgbot-actions
Телеграм бот для рассылки уведомлений о результатах тестирования


1. Add python libs:
	1. pip install aiogram
	2. pip install poplib
	3. pip install yaml


2. Создание телеграм бота: пишем @BotFather

	1. GitHub actions Nadya222 (какое-то такое название).


3. Настройки гугл:

	1. Создаем аккаунт гугл, nadacernavskaya@gmail.com, к примеру.

	2. Разрешаем логиниться боту в аккаунт:
	Управление аккаунтом > Безопастность > Ненадежные приложения, у которых есть доступ к аккаунту
	Переключаем свич.
	
	3. На странице https://github.com/settings/emails добавьте ту почту, на которую хотите получать уведомления о сборках проекта.


4. Конфигурация бота:
	1. Записать параметры авторизации для почты и токен от бота в конфиг ./cnf.yml, в 'user' свой id в tg
	2. Сменить в ./*.py значение параметра config_path с "config.yml" на нужный (config_path = "cnf.yml")
	3. 


5. Настройка сервера:
root@sampc:~# mkdir /usr/bin/tgbot-actions
root@sampc:~# cd /home/samson/tgbot-actions
root@sampc:/home/samson/tgbot-actions# ls
bot.service  config.yml    mail_checker.service  main.py      README.md
cnf.yml      get_mails.py  mails_manager.py      __pycache__
root@sampc:/home/samson/tgbot-actions# cp get_mails.py /home/samson/tgbot-actions
cp: 'get_mails.py' и '/home/samson/tgbot-actions/get_mails.py' - один и тот же файл
root@sampc:/home/samson/tgbot-actions# cp get_mails.py /usr/bin/tgbot-actions
root@sampc:/home/samson/tgbot-actions# cp mails_manager.py /usr/bin/tgbot-actions
root@sampc:/home/samson/tgbot-actions# cp main.py /usr/bin/tgbot-actions
root@sampc:/home/samson/tgbot-actions# mkdir /etc/tgbot-actions
root@sampc:/home/samson/tgbot-actions# cp config.yml /etc/tgbot-actions
root@sampc:/home/samson/tgbot-actions# cp get_mails.py /usr/bin/tgbot-actions
root@sampc:/home/samson/tgbot-actions# cp mails_manager.py /usr/bin/tgbot-actions
root@sampc:/home/samson/tgbot-actions# cp main.py /usr/bin/tgbot-actions

