import telebot
import config
bot=telebot.TeleBot(config.token)

@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
        bot.send_message(message.chat.id,'Привет, это ПАПА')
        
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text=='Привет':
         bot.send_message(message.from_user.id,'Привет, кагдила?')
    else:
        bot.send_message(message.from_user.id,'Ну да')
bot.polling(none_stop=True,interval=0)
