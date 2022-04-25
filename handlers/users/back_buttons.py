from aiogram.types import CallbackQuery

from keyboards.inline.inline_menu import main_menu
from loader import dp, db


@dp.callback_query_handler(text='back_category')
async def back_category(call: CallbackQuery):
    category_list = await db.get_category()
    btn = main_menu(category_list)
    await call.message.edit_text(f"Bo'limlardan birini tanlang: ", reply_markup=btn)


@dp.callback_query_handler(text=["back_tv", "back_audio", "back_photo_video",
                                 "back_noutbook", "back_monitor", "back_monoblok", "back_smartfon",
                                 "back_sm_gadjets", "back_washing_machine", "back_air_conditioner"])
async def back_subcategory(call: CallbackQuery):
    subcategory_code = (call.data).split('back_')[1]
    subcategory_list = await db.back_subcategory(subcategory_code)
    subcategory_name = await db.back_subcategory_name(subcategory_code)
    btn = main_menu(subcategory_list, subcategory=True)

    await call.message.edit_text(subcategory_name, reply_markup=btn)


@dp.callback_query_handler(text=['back_product_list_' + str(i) for i in range(1, 101)])
async def back_product_list(call: CallbackQuery):
    product_id = int(call.data.split('back_product_list_')[1])
    product_list = await db.back_product_list(product_id)
    subcategory_code = await db.get_subcategory_code_from_id(product_id)
    subcategory_name = await db.get_subcategory_name(subcategory_code)
    btn = main_menu(product_list, subcategory_code, product=True)
    await call.message.edit_text(subcategory_name, reply_markup=btn)
