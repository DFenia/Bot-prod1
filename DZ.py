import requests
from gettext import find
import bs4
import telebot
from telebot import types

def f1(bot, chat_id):
    bot.send_message(chat_id, "ФОТО-1")
    img = open('кот1.jpg', 'rb')
    bot.send_photo(chat_id, img)

def f2(bot, chat_id):
    bot.send_message(chat_id, "ФОТО-2")
    img = open('кот1.jpg', 'rb')
    bot.send_photo(chat_id, img)

def f3(bot, chat_id):
    bot.send_message(chat_id, "ФОТО-3")
    img = open('кот1.jpg', 'rb')
    bot.send_photo(chat_id, img)

    #bot.send_message(chat_id, "Автор: CatBadBed")
    #markup = types.InlineKeyboardMarkup()
    #btn1 = types.InlineKeyboardButton(text="Напишите автору", url="https://t.me/CatBadBed")
    #markup.add(btn1)
    #img = open('кот1.jpg', 'rb')
    #bot.send_photo(chat_id, img, reply_markup=markup)
