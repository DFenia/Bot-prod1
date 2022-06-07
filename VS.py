import requests
from gettext import find
import bs4
import telebot
from telebot import types

def F(bot, chat_id):
    bot.send_message(chat_id, "Здесь вы можете купать 1 и 2 часть из моего фотосета (фотки не повторяются). Каждый из наборов включает в себя 15 фото за 250 рубелй.")
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text="Купить 1й набор", url="https://t.me/CatBadBed")
    markup.add(btn1)
    btn2 = types.InlineKeyboardButton(text="Купить 2й набор", url="https://t.me/CatBadBed")
    markup.add(btn2)
    img = open('кот1.jpg', 'rb')
    bot.send_photo(chat_id, img, reply_markup=markup)



def KV(bot, chat_id):
    bot.send_message(chat_id, "Здесь вы можете купить 1 и 2 наборы коротких видео (видео не повторяются, от 15 до 45 секунд). Каждый из наборов включает в себя 3 фото за 250 рубелй.")
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text="Купить 1й набор", url="https://t.me/CatBadBed")
    markup.add(btn1)
    btn2 = types.InlineKeyboardButton(text="Купить 2й набор", url="https://t.me/CatBadBed")
    markup.add(btn2)
    img = open('кот1.jpg', 'rb')
    bot.send_photo(chat_id, img, reply_markup=markup)

def DV(bot, chat_id):
    bot.send_message(chat_id, "Здесь вы можете выбрать 1 из 13 видео. Цена варьируется от 200 до 300 рублей:")
    bot.send_message(chat_id, "1-")
    bot.send_message(chat_id, "2-")
    bot.send_message(chat_id, "3-")
    bot.send_message(chat_id, "4-")
    bot.send_message(chat_id, "5-")
    bot.send_message(chat_id, "6-")
    bot.send_message(chat_id, "7-")
    bot.send_message(chat_id, "8-")
    bot.send_message(chat_id, "9-")
    bot.send_message(chat_id, "10-")
    bot.send_message(chat_id, "11-")
    bot.send_message(chat_id, "12-")
    bot.send_message(chat_id, "13-")
    bot.send_message(chat_id, "ПОЖАЛУЙСТА В КОММЕНТАРИИ К ПЛАТЕЖУ УКАЖИТЕ НОМЕР ВИДЕО В ФОРМАТЕ - ДВ(номер видео)")
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text="1-", url="https://t.me/CatBadBed")
    markup.add(btn1)
    btn2 = types.InlineKeyboardButton(text="2-", url="https://t.me/CatBadBed")
    markup.add(btn2)
    btn3 = types.InlineKeyboardButton(text="3-", url="https://t.me/CatBadBed")
    markup.add(btn3)
    btn4 = types.InlineKeyboardButton(text="4-", url="https://t.me/CatBadBed")
    markup.add(btn4)
    btn5 = types.InlineKeyboardButton(text="5-", url="https://t.me/CatBadBed")
    markup.add(btn5)
    btn6 = types.InlineKeyboardButton(text="6-", url="https://t.me/CatBadBed")
    markup.add(btn6)
    btn7 = types.InlineKeyboardButton(text="7-", url="https://t.me/CatBadBed")
    markup.add(btn7)
    btn8 = types.InlineKeyboardButton(text="8-", url="https://t.me/CatBadBed")
    markup.add(btn8)
    btn9 = types.InlineKeyboardButton(text="9-", url="https://t.me/CatBadBed")
    markup.add(btn9)
    btn10 = types.InlineKeyboardButton(text="10-", url="https://t.me/CatBadBed")
    markup.add(btn10)
    btn11 = types.InlineKeyboardButton(text="11-", url="https://t.me/CatBadBed")
    markup.add(btn11)
    btn12 = types.InlineKeyboardButton(text="12-", url="https://t.me/CatBadBed")
    markup.add(btn12)
    btn13 = types.InlineKeyboardButton(text="13-", url="https://t.me/CatBadBed")
    markup.add(btn13)
    img = open('кот1.jpg', 'rb')
    bot.send_photo(chat_id, img, reply_markup=markup)

def FF(bot, chat_id):
    bot.send_message(chat_id, "...")
