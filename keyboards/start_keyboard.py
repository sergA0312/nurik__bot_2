from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)


async def start_kb():
    quiz_button = KeyboardButton("/quiz")
    mark_up = ReplyKeyboardMarkup(one_time_keyboard=True,
                                  resize_keyboard=True)

    mark_up.add(quiz_button)
    return mark_up


async def quiz_1_keyboard():
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton(
        "Следующая Викторина",
        callback_data="button_call_1"
    )
    markup.row(
        button_call_1
    )
    return markup


async def quiz_2_keyboard():
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton(
        "Male",
        callback_data="answer_male"
    )
    button_call_2 = InlineKeyboardButton(
        "Female",
        callback_data="answer_female"
    )
    markup.row(
        button_call_1,
        button_call_2
    )
    return markup


async def admin_select_user_keyboard():
    markup = InlineKeyboardMarkup()
    admin_user_list = InlineKeyboardButton(
        "Список пользователей",
        callback_data="admin_user_list"
    )

    markup.row(
        admin_user_list
    )
    return markup