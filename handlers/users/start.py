from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.inline.inline_menu import main_menu
from loader import dp, db


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    chat_id = message.from_user.id
    await db.create_user(chat_id)

    user_status = await db.user_info(chat_id)

    if not user_status:
        await message.answer(f"Assalomu aleykum, Online Do'konga xush kelibsiz!\n\n"
                             f"Ro'yxatdan o'tish uchun /registration komandasini bosing.")
    else:
        category_list = await db.get_category()
        btn = main_menu(category_list)
        await message.answer(f"Bo'limlardan birini tanlang: ", reply_markup=btn)
