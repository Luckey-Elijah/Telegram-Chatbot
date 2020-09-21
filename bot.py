import requests
import json
import configparser as cfg


class TelegramChatbot():
    def read_token_from_config_file(self, config_file):
        parser = cfg.ConfigParser()
        parser.read(config_file)
        return parser.get('creds', 'token')

    def __init__(self, config_file):
        self.token = read_token_from_config_file(self, config_file)
        self.base = "https://api.telegram.org/bot{}/".format(self.token)

    def get_updates(self, offset=None):
        url = self.base + "/getUpdates?timeout=100"
        if offset:
            url = url + "&offset={}".format(offset + 1)
        response = requests.get(url)
        return json.loads(response.content)

    def send_message(self, msg, chat_id):
        url = self.base + "sendMessage?chat_id={}&text={}".format(chat_id, msg)
        if msg is not None:
            requests.get(url)
