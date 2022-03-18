import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
import time, requests, json
import datetime as dt
import CoinbaseProAUTH
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from telegram import InlineQueryResultArticle, InputTextMessageContent
import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext
import datetime
import shrimpy
import plotly.graph_objects as go
import pathlib

telegram_bot_token = "1217098424:AAHLrZMDsutjCr1MpLJxplp1d66Qlydxsrk"

updater = Updater(token=telegram_bot_token, use_context=True)
dispatcher = updater.dispatcher

up = Update
mes = "Project by Alessandro Cicola \n[Please don't type commands. The bot won't reply (I'm updating :D)]"

#-------------------------------/start-------------------------------
def start(update, context):
	global up
	up = update
	chat_id = update.effective_chat.id
	context.bot.send_message(chat_id=chat_id, text=mes)
	generaMenu(update)

def generaMenu(update):
    update.message.reply_text('I valori sono estratti dal sito pro.coinbase.com \n', reply_markup=main_menu_keyboard())

def main_menu_keyboard():
  keyboard = [[InlineKeyboardButton('START', callback_data='main')]]
  return InlineKeyboardMarkup(keyboard)

#-------------------------------aggiorna valori-------------------------------
def currency(update, context):
        while True:
            try:
                message = CoinbaseProAUTH.finalMEX()
                query = update.callback_query
                query.edit_message_text(text=message, reply_markup="")
                query.answer()
            except:
                pass


dispatcher.add_handler(CommandHandler("currency", currency))
dispatcher.add_handler(CommandHandler("start", start))
updater.dispatcher.add_handler(CallbackQueryHandler(currency, pattern='main'))

updater.start_polling()
