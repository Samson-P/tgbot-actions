import yaml, poplib


config_path = "/etc/tgbot-actions/config.yml"


def get_meta(cmd):
	with open(config_path, 'r') as config_file:
		config = yaml.load(config_file, Loader=yaml.BaseLoader)
	return config[cmd]


def mail_manager():
	pop_conn = poplib.POP3_SSL('pop.gmail.com')
	pop_conn.user(get_meta('login'))
	pop_conn.pass_(get_meta('passwd'))
	messages = [pop_conn.retr(i) for i in range(1, len(pop_conn.list()[1]) + 1)]
	response = []
	
	for message in messages:
		for line in message[1]:
			if str(line.decode())[0:7] == "Subject":
				response.append(
					str(line.decode()).split('Subject: ')[1] + 
					str(message[1][message[1].index(line) + 1].decode())
				)
	
	pop_conn.quit()
	
	if len(response) == 0:
		return None, 'Sorry, no updates :('
	return response, None


if __name__ == '__main__':
	response, err = mail_manager()
	if err == None:
		[print(msg) for msg in response]
	else:
		print(err)
