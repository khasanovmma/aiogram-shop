from aiogram.types import CallbackQuery, InlineKeyboardButton

from keyboards.inline.inline_menu import main_menu
from loader import dp, db


@dp.callback_query_handler(text=["tvtexno", "comp", "phone", "homeAppliances"])
async def subcategory(call: CallbackQuery):
    await call.answer()
    subcategory_code = call.data
    subcategory_list = await db.get_subcategory(subcategory_code)
    category_name = await db.get_category_name(subcategory_code)
    btn = main_menu(subcategory_list, subcategory=True)
    await call.message.edit_text(category_name, reply_markup=btn)
