# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 13:50:05 2022

@author: User
"""


from transliterate import to_cyrillic,to_latin 
import telebot

TOKEN = '5091729283:AAHniWKFX97_aWz0NdNYrcv6bSgnjMj04S0'

bot = telebot.TeleBot(TOKEN, parse_mode=None) 



@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    answer = "Assalomu aleykum hush kelibsiz!!! Siz o'zbek kirill botiga murojaat qildingiz!! \nSiz bu botga lotin alifbosida ma'lumot kiritsangiz kirill alifbosiga o'tkazib beradi,agar kirill alifbosida yozsangiz lotinga ozgartirib beradi!\nIltimos ma'lumot kiriting: "
    bot.reply_to(message, answer)


    
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    newMessage = message.text
    if newMessage.isascii():
        newMessage = to_cyrillic(newMessage)
    else:
        newMessage = to_latin(newMessage) 
    bot.reply_to(message,newMessage)


bot.infinity_polling()


 












