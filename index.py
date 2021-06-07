import telepot, requests
from telepot.loop import MessageLoop

TOKEN = 'TOKEN_GERADO_BOTFATHER'
URL = 'URL_API'

bot = telepot.Bot(TOKEN)

def handle(msg):
    if "text" in msg:
        try:
            data = {'message_id': msg['message_id'], 'id': msg['from']['id'], 'first_name': msg['chat']['first_name'], 'last_name': msg['chat']['last_name'], 'date': msg['date'], 'text': msg['text']}
            x = requests.post(URL, data = data)
            bot.sendMessage(msg["from"]["id"], "Reply: mensagem recebida")
        except:
            bot.sendMessage(msg["from"]["id"],"Error.")
    else:
        bot.sendMessage(msg["from"]["id"],"Comando Inválido.")

MessageLoop(bot, handle).run_as_thread()

while True:
    pass