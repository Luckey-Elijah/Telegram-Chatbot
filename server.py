from bot import TelegramChatbot as bot
import json
from typing import Final

update_id = None
RESULT_KEY: Final = "result"
MESSAGE_KEY: Final = "message"
CONFIG_FILE = "token.cfg"


def make_reply(message):
    if message is not None:
        reply = "Okay"
    return reply


while True:
    print("...")
    b = bot(CONFIG_FILE)
    updates = b.get_updates(offset=update_id)
    updates = updates[RESULT_KEY]
    if updates:
        for item in updates:
            update_id = item["update_id"]
            try:
                # fetching message content form Json
                message = item[MESSAGE_KEY]["text"]
            except ValueError():
                message = None
            # gets the id of the person who sent the message
            # to the bot
            from_ = item[MESSAGE_KEY]["from"]["id"]

            reply = make_reply(message)
            print('REPLYING TO:', item[MESSAGE_KEY]["from"]["username"])
            print('REPLYING:', reply)
            b.send_message(reply, from_)
