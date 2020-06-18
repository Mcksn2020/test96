import telebot
import config
import ggchrt
from telebot import types

bot=telebot.TeleBot(config.token)

key0 = types.InlineKeyboardMarkup()
k_btn11=types.InlineKeyboardButton('Voc',callback_data='Voc')
k_btn12=types.InlineKeyboardButton('Standard Strategy',callback_data='SS')
k_btn13=types.InlineKeyboardButton('Build Your Strategy',callback_data='BYS')
k_btn14=types.InlineKeyboardButton('Quiz Strategy',callback_data='QS')
key0.add(k_btn11)
key0.add(k_btn12)
key0.add(k_btn13)
key0.add(k_btn14)

#keyboard0.row('Voc', 'Standard Srategy','Build You Strategy','Quiz Strategy')

@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
        bot.send_message(message.chat.id,'Привет, это ПАПА'
        ,reply_markup=key0)
        
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

