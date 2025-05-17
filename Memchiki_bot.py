import telebot
from telebot.types import InlineKeyboardMarkup
from telebot import types
import os

bot = telebot.TeleBot(os.environ.get("BOT_TOKEN"))


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привіт це бот про Англійську')


@bot.message_handler(commands=['book'])
def book(message):
    markup  =  types.InlineKeyboardMarkup()
    knopka1  = types.InlineKeyboardButton('A1/A2', callback_data='A1/A2')
    knopka2  = types.InlineKeyboardButton('A2+/B1', callback_data='A2+/B1')
    knopka3  = types.InlineKeyboardButton('B1/B1+',callback_data='B1/B1+')
    knopka4 = types.InlineKeyboardButton('B2/B2+',callback_data='B2/B2+')
    knopka5 = types.InlineKeyboardButton('B2+/C1',callback_data='B2+/C1')
    markup.add(knopka1, knopka2 , knopka3,knopka4,knopka5)
    bot.send_message(message.chat.id ,"Оберіть рівень англійської", reply_markup=markup)




@bot.callback_query_handler(func=lambda call:True)
def handle_calllback_query(call):
    if call.data == 'A1/A2':
        bot.answer_callback_query(call.id,"Ви обрали A1/A2!")
        bot.send_message(call.message.chat.id,"https://www.at.alleng.org/d/engl_en/eng672.htm")
    elif call.data == 'A2+/B1':
        bot.answer_callback_query(call.id,"Ви обрали A2+/B1!")
        bot.send_message(call.message.chat.id,"https://www.at.alleng.org/d/engl_en/eng673.htm")

    elif call.data == 'B1/B1+':
        bot.answer_callback_query(call.id, "Ви обрали B1/B1+!")
        bot.send_message(call.message.chat.id, "https://www.at.alleng.org/d/engl_en/eng674.htm")

    elif call.data == 'B2/B2+':
        bot.answer_callback_query(call.id, "Ви обрали B2/B2+!")
        bot.send_message(call.message.chat.id, "https://www.at.alleng.org/d/engl_en/eng675.htm")

    elif call.data == 'B2+/C1':
        bot.answer_callback_query(call.id, "Ви обрали B2+/C1!")
        bot.send_message(call.message.chat.id, "https://www.at.alleng.org/d/engl_en/eng676.htm")



bot.polling(none_stop=True)