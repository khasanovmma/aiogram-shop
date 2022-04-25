from aiogram.types import CallbackQuery

from keyboards.inline.inline_menu import generate_menu
from loader import dp, db


@dp.callback_query_handler(text=['categories', 'back_categories'])
async def categories(call: CallbackQuery):
    await call.answer()
    category_list = await db.get_category()
    button = await generate_menu(category_list, main=True)
    await call.message.edit_text("Bo'limlardan birini tanlang:", reply_markup=button)
