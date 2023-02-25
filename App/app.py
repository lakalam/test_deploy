#pylint: disable=W0311
import telebot
bot=telebot.TeleBot('6100720154:AAFQtSQgy85DpX4o0U88G5LYxTrrHReEbTo')
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
 if message.text=="Привет":
    bot.send_message(message.from_user.id,"Привет, чем я могу тебе помочь?")
 elif message.text=="/help":
    bot.send_message(message.from_user.id,"PIPSKA")
 else:
    bot.send_message(message.from_user.id,"Я тебя не понимаю. Напиши PIPSKA!!!!.")