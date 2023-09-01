from aiogram.utils import executor
from config import dp
import handlers
from database.sql_commands import Database


async def on_start_up(_):
    db = Database()
    db.sql_create_db()


fs.start.register_start_handlers(dp=dp)
handlers.callback.register_callback_handlers(dp=dp)
handlers.reference.register_reference_handlers(dp=dp)
handlers.register_fsm_form_handlers(dp=dp)
handlers.chat_actions.register_chat_actions_handlers(dp=dp)

if __name__ == "__main__":
    executor.start_polling(dp,
                           skip_updates=True,
                           on_startup=on_start_up)