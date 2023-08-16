from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)


async def my_profile_keyboard():
    markup = InlineKeyboardMarkup()
    my_profile_button = InlineKeyboardButton(
        "Мой Профиль",
        callback_data="my_profile"
    )

    markup.add(
        my_profile_button
    )
    return markup