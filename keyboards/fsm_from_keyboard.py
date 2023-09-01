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

async def new_start_kb():
    markup = InlineKeyboardMarkup()
    random_profiles_button = InlineKeyboardButton(
        "Анкеты для просмотра",
        callback_data="random_profiles"
    )
    my_profile_button = InlineKeyboardButton(
        "Мой Профиль",
        callback_data="my_profile"
    )

    markup.row(
        random_profiles_button,
        my_profile_button
    )
    return markup


async def like_dislike_profiles_keyboard(form_telegram_id):
    markup = InlineKeyboardMarkup(row_width=2)
    like_button = InlineKeyboardButton(
        "👍🏻",
        callback_data=f"like_{form_telegram_id}"
    )
    dislike_button = InlineKeyboardButton(
        "👎🏻",
        callback_data="random_profiles"
    )
    markup.row(
        like_button,
        dislike_button
    )
    return markup


async def my_profile_detail_keyboard(telegram_id):
    markup = InlineKeyboardMarkup(row_width=2)
    update_button = InlineKeyboardButton(
        "Изменить Анкету 💡",
        callback_data="signup"
    )
    delete_button = InlineKeyboardButton(
        "Удалить Анкету ❌",
        callback_data=f"delete_form_{telegram_id}"
    )
    markup.row(
        update_button,
        delete_button
    )
    return markup