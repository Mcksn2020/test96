import telebot
import config
import ggchrt
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
         bot.send_document(message.from_user.id,ggchrt.gc1)
         bot.send_document(message.from_user.id,ggchrt.gc2)
         bot.send_document(message.from_user.id,ggchrt.gc3)
    else:
        bot.send_message(message.from_user.id,'Ну да')
bot.polling(none_stop=True,interval=0)
