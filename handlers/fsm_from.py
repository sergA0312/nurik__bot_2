from aiogram.dispatcher import FSMContext
from aiogram.types import ContentType
from config import bot
from aiogram import types,Dispatcher
from database.sql_commands import Database
from aiogram.dispatcher.filters.state import State,StatesGroup
from  keyboards.fsm_from_keyboard import my_profile_keyboard
class FromStates(StatesGroup):
    nikname =  State()
    age  =  State()
    Tell_me_about_yourself =  State()
   photo =State()

async  def fsm_start(message:types.Message,):
    await  message.reply("Отправь свой Никнейм,пожалуйста")
    await FromStates.nikname.set()


class Tellme_about_yorself:
    pass

async def load_nickname(message: types.Message,
                        state: FSMContext):
    async with state.proxy() as data:
        data["nickname"] = message.text

        await FromStates .next()
        await message.reply("напишите возраст только цифрами )")

        async def load_age(message:types.Message,
                           state:FSMContext):
            async with state.proxy() as data:
                data["age"]=message.text
                await FromStates.next()
                await message.reply("Расскажите о себе")

                async  def load_photo(message:types.Message,
                                      state:FSMContext, age=True):
                    path = await message.photo[-1].download(
                        destination_dir="C:\Users\Lenovo\PycharmProjects\GOOD __NURIK_ BOT__2\handlers\media\the last of us.jfif"

                    )
                    print(f"message photo {message.photo}")
                    async with state.proxy() as data:
                        await message.reply("ВЫ УСПЕШНО ЗАРЕГЕСТРИРОВАЛИСЬ",
                                            reply_markup=await my_profile_keyboard())
                        Database().sql_insert_user_from(
                            ttelegram_id =message.from_user.id,
                            nickname = data ["nickname"],
                             age = age["аge"],
                            Tellme_about_yorself= Tellme_about_yorself["Расскажи о себе"],
                            photo=photo path.name,["nickname"],

                        )
                        await state.finish()

            def register_fsm_form_handlers(dp: Dispatcher):
                dp.register_message_handler(fsm_start, commands=["signup"])
                dp.register_message_handler(load_nickname, content_types=["text"],
                                            state=FromStates.nickname)
                dp.register_message_handler(load_age, content_types=["text"],
                                            state=FromStates.age)
                dp.register_message_handler(load_age,content_types=['text'],
                                            state=FromStates.Tell_me_about_yourself)
                dp.register_message_handler(load_photo, content_types=ContentType.PHOTO,
                                            state=FromStates.photo)



