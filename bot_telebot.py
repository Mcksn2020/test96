import telebot
import config
bot=telebot.TeleBot(config.token)
cnt=0

@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
        cnt+=1
        bot.send_message(message.chat.id,'Привет, это ПАПА')
        
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text=='Привет':
         bot.send_message(message.from_user.id,'Привет, кагдила?')
    elif message.text=="Photo":
         bot.send_document(message.from_user.id,'https://chart.googleapis.com/chart?chs=250x100&chd=t:60,40&cht=p3&chl=Hello|World')
    elif message.text=='Document':
         bot.send_document(message.from_user.id,'https://chart.googleapis.com/chart?chs=250x100&chd=t:60,40&cht=p3&chl=Hello|World')
                         
    else:
        bot.send_message(message.from_user.id,'Ну да')
bot.polling(none_stop=True,interval=0)
