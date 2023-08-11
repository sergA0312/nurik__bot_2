# command_handlers.py
from telegram.ext import сommandHandler
from config import config
from database import db_utils

def start(update, context):
    user_id = update.message.from_user.id
    username = update.message.from_user.username

    db_utils.insert_user(user_id, username)
    update.message.reply_text("Привет! Ты был записан в базу данных.")

start_handler = CommandHandler('start', start)
