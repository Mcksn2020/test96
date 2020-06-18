import telebot
import config
import ggchrt
from telebot import types

cnt_d=0

bot=telebot.TeleBot(config.token)

keyboard0 = types.ReplyKeyboardMarkup()
keyboard0.row('Voc', 'Standard Srategy') #,'Build You Strategy','Quiz Strategy')

@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
        cnt_d+=1
        bot.send_message(message.chat.id,'Привет, это ПАПА'
        ,reply_markup=keyboard0)
        
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text=='Привет':
         bot.send_message(message.from_user.id,'Привет, кагдила?')
    elif message.text=="Photo":
         bot.send_document(message.from_user.id,ggchrt.gc)
         #bot.send_document(message.from_user.id,ggchrt.gc2)
         #bot.send_document(message.from_user.id,ggchrt.gc3)
    else:
        bot.send_message(message.from_user.id,'Ну да')
bot.polling(none_stop=True,interval=0)
