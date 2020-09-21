from bot import TelegramChatbot as bot

update_id = None


def make_reply(message):
    if message is not None:
        reply = "Okay"
    return reply


while True:
    print("...")
    b = bot("config.cfg")
    updates = b.get_updates(offset=update_id)
    updates = updates["results"]
    if updates:
        for item in updates:
            update_id = item["update_id"]
            try:
                # fetching message content form Json
                message = item["message"]["text"]
            except ValueError():
                message = None
            # gets the id of the person who sent the message
            # to the bot
            from_ = item["message"]["from"]["id"]
            reply = make_reply(message)
            bot.send_message(reply, from_)
