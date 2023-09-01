from datetime import timedelta

from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot
from database.sql_commands import Database


async def echo_ban(message: types.Message, datetime=None):
    ban_words = ["небегающиийhttps://github.com/sergA0312/nurik__bot_2__.git", "fuck", 'bitch']

    if message.chat.id == -833914033:
        for word in ban_words:
         if word in message.text.lower().replace(" ", ""):
            await bot.delete_message(
                chat_id=message.chat.id,
                message_id=message.message_id
            )
            await bot.send_message(
                chat_id=message.chat.id,
                text=f"Сам ты такой, {message.from_user.username}!"
            )
            existing = Database().select_users_ban(telegram_id=message.from_user.id)
            if existing:
                Database().update_ban_users_count(telegram_id=message.from_user.id)
            else:
                Database().insert_ban_users_count(
                    telegram_id=message.from_user.id,
                    bancount=1)
            counts = Database().select_users_counts(telegram_id=message.from_user.id)
            await bot.send_message(chat_id=message.chat.id,
                                   text=f'Ваше {counts[0]} предупреждение'
                                   )
            if counts[0] == 3:
                ban_time = datetime.timedelta(minutes=1)
                await bot.ban_chat_member(
                    chat_id=message.chat.id,
                    user_id=message.from_user.id,
                    until_date=ban_time
                )
                await bot.send_message(chat_id=message.chat.id,
                                       text=f"Пользователь {message.from_user.username}"
                                            f"\nбыл забанен на {ban_time}")
                Database().delete_banned_users(
                    telegram_id=message.from_user.id
                )
            # await bot.ban_chat_member(
            #     chat_id=message.chat.id,
            #     user_id=message.from_user.id,
            #     until_date=datetime.now + timedelta(minutes=1)
            # )


def register_chat_actions_handlers(dp: Dispatcher):
    dp.register_message_handler(echo_ban)
