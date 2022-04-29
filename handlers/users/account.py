from aiogram.types import CallbackQuery

from filters import IsPrivate
from keyboards.inline.inline_menu import generate_menu
from loader import dp, db


@dp.callback_query_handler(IsPrivate(), text='my_account')
async def my_account(call: CallbackQuery):
    chat_id = call.from_user.id
    full_name = await db.user_info(chat_id)
    btn = await generate_menu(main=True)
    await call.message.edit_text(full_name, reply_markup=btn)
    
