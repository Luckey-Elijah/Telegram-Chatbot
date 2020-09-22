import requests
import json
import configparser as cfg


class TelegramChatbot():
    def __init__(self, config_file):
        def read_token_from_config_file(self, config_file):
            # this is an object method
            # so it must be declare globally
            # or within init
            parser = cfg.ConfigParser()
            parser.read(config_file)
            return parser.get('creds', 'token')
        self.token = read_token_from_config_file(self, config_file)
        self.base = "https://api.telegram.org/bot{}/".format(self.token)

    def get_updates(self, offset=None):
        url = self.base + "getUpdates?timeout=100"
        if offset:
            url = url + "&offset={}".format(offset + 1)
        response = requests.get(url)
        return json.loads(response.content)

    def send_message(self, message, chat_id):
        # creates the url response
        url = self.base + \
            "sendMessage?chat_id={}&text={}".format(chat_id, message)

        # pings the telegram api with teh url when empty
        if message is not None:
            requests.get(url)
