import datetime
import re
from aiogram.dispatcher import FSMContext
from config import bot
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from aiogram import types, Dispatcher
from database.sql_commands import Database
from aiogram.dispatcher.filters.state import State, StatesGroup
from database.sql_commands import Database


class ReportUser(StatesGroup):
    report = State()
    reason = State()

class Username(StatesGroup):
    username = State()




async def report_message_button():
    markup = InlineKeyboardMarkup()
    chance_button = InlineKeyboardButton('Возможность',
                                         callback_data='chance')
    pass_button = InlineKeyboardButton('cкипнуть',
                                       callback_data='pass_button')
    markup.row(chance_button,
               pass_button)
    return markup


async def start_report_fsm(message: types.Message):
    await bot.delete_message(chat_id=message.chat.id,
                             message_id=message.message_id)
    await bot.send_message(chat_id=message.chat.id,
                           text='Введите @username  или firstname пользователя,'
                                '\nчтобы отправить жалобу')
    await ReportUser.report.set()



async def report_to_user(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        report_username = re.sub("@","", message.text)
        data['report'] = report_username
        await bot.delete_message(chat_id=message.chat.id,
                                 message_id=message.message_id)
        await bot.send_message(chat_id=message.chat.id,
                               text='Введите причину жалобы')
        await ReportUser.reason.set()


async def load_reason(message: types.Message,state: FSMContext):
    await bot.delete_message(chat_id=message.chat.id,
                             message_id=message.message_id)
    async with state.proxy() as data:
        data['reason'] = message.text
    bad_user_id_by_firstname= Database().sql_select_tg_user_by_firstname(firstname=data['report'])
    bad_user_id_by_username= Database().sql_select_tg_user_by_username(username=data['report'])
    if bad_user_id_by_username:
        existing = Database().sql_select_existing_bad_user(telegram_id_bad_user=bad_user_id_by_username[0]['telegram_id'])
        if existing:
            Database().sql_update_user_complain(telegram_id_bad_user=bad_user_id_by_username[0]['telegram_id'])
            await bot.send_message(chat_id=message.chat.id,
                                   text='Ваша жалоба принята!')
            await state.finish()
        else:
            Database().sql_insert_user_complain(username_first_who_complained=message.from_user.first_name,
                                                telegram_id_complained_user=message.from_user.id,
                                                telegram_id_bad_user=bad_user_id_by_username[0]['telegram_id'],
                                                reason=data['reason'],
                                                count=1)
            await message.reply('Ваша жалоба принята')
            await state.finish()
        counts = Database().sql_select_report_count(bad_user_id_by_username[0]['telegram_id'])
        if counts[0]['report_count'] >= 3:
            ban_time = datetime.timedelta(minutes=200)
            await bot.ban_chat_member(
                chat_id=message.chat.id,
                user_id=bad_user_id_by_username[0]['telegram_id'],
                until_date=ban_time
            )
            await bot.send_message(chat_id=message.chat.id,
                                   text=f"Пользователь "
                                        f"\nбыл забанен на {ban_time}")
            Database().sql_delete_reported_banned_users(bad_user_id_by_username[0]['telegram_id'])
        await bot.send_message(chat_id=bad_user_id_by_username[0]['telegram_id'],
                                text='На вас была отправлена жалоба!',
                               reply_markup= await report_message_button()
                                )
    elif bad_user_id_by_firstname:
        existing = Database().sql_select_existing_bad_user(
            telegram_id_bad_user=bad_user_id_by_firstname[0]['telegram_id'])
        if existing:
            Database().sql_update_user_complain(telegram_id_bad_user=bad_user_id_by_firstname[0]['telegram_id'])
            await bot.send_message(chat_id=message.chat.id,
                                   text='Ваша жалоба принята спасибо за обращение!')
            await state.finish()
        else:
            Database().sql_insert_user_complain(username_first_who_complained=message.from_user.first_name,
                                                telegram_id_complained_user=message.from_user.id,
                                                telegram_id_bad_user=bad_user_id_by_firstname[0]['telegram_id'],
                                                reason=data['reason'],
                                                count=1)
            await message.reply('Ваша жалоба принята')
            await state.finish()
        counts = Database().sql_select_report_count(bad_user_id_by_firstname[0]['telegram_id'])
        if counts[0]['report_count'] >= 3:
            ban_time = datetime.timedelta(minutes=1)
            await bot.ban_chat_member(
                chat_id=message.chat.id,
                user_id=bad_user_id_by_firstname[0]['telegram_id'],
                until_date=ban_time
            )
            await bot.send_message(chat_id=message.chat.id,
                                   text=f"Пользователь "
                                        f"\nбыл забанен на {ban_time}")
            Database().sql_delete_reported_banned_users(bad_user_id_by_firstname[0]['telegram_id'])
        await bot.send_message(chat_id=bad_user_id_by_firstname[0]['telegram_id'],
                               text='На вас была отправлена жалоба хех)',
                               reply_markup=await report_message_button()
                               )

    else:
        await message.reply('Вы ввели неверный @username или firstname')
        await state.finish()









def register_report_handler(dp: Dispatcher):
    dp.register_message_handler(start_report_fsm, commands=['report'])
    dp.register_message_handler(report_to_user,content_types=['text'],state=ReportUser.report)
    dp.register_message_handler(load_reason,content_types=['text'],state=ReportUser.reason)




