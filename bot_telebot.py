import telebot
import config
import ggchrt
from telebot import types

bot=telebot.TeleBot(config.token)

keyboard0 = types.ReplyKeyboardMarkup(True)
keyboard0.row('Voc', 'Standard Srategy','Build You Strategy','Quiz Strategy')

@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
        bot.send_message(message.chat.id,'Привет, это ПАПА'
        ,reply_markup=keyboard0)
        
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text=='Привет':
         bot.send_message(message.from_user.id,'Привет, кагдила?')
    elif message.text=="Photo":
         bot.send_document(message.from_user.id,ggchrt.gc)
    else:
        bot.send_message(message.from_user.id,'Ну да')

@bot.callback_query_handler(func=lambda call:True)
def btn_answer (call):
     if call.data=='Voc':
             bot.send_message(call.message.chat.id,'Словаря пока нет ')
             
bot.polling(none_stop=True,interval=0)

