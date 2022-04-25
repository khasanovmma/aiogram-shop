from aiogram.types import CallbackQuery

from keyboards.inline.inline_menu import main_menu
from loader import dp, db

@dp.callback_query_handler(text=["tv", "audio", "photo_video",
                                 "noutbook","monitor", "monoblok", "smartfon",
                                 "sm_gadjets","washing_machine", "air_conditioner"])
async def product(call: CallbackQuery):
    await call.answer()
    subcategory_code = call.data
    product_list = await db.get_product_list(subcategory_code)
    subcategory_name = await db.get_subcategory_name(subcategory_code)
    btn = main_menu(product_list, product=True, product_subcategory_code=subcategory_code)

    await call.message.edit_text(subcategory_name, reply_markup=btn)
