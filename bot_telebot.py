import telebot
from telebot import apihelper
apihelper.proxy={'https':'socks5h://userproxy:password@proxy_address:port'}
bot=telebot.TeleBot('1252740921:AAHHgCl3AZVc--cK-Lz1P9uxZraponCpmZc')
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text=='Привет':
         bot.send_message(message.from_user.id,'Привет, это ПАПА, кагдила?')
    else:
        bot.send_message(message.from_user.id,'Ну да')
bot.polling(none_stop=True,interval=0)
