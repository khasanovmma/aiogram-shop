from aiogram.types import CallbackQuery

from keyboards.inline.inline_menu import product
from loader import dp, db


@dp.callback_query_handler(text=[i for i in range(1, 101)])
async def view_product(call: CallbackQuery):
    await call.answer()
    product_id = call.data
    data = await db.get_product_by_id(product_id)
    product_name, product_photo, product_desc, product_price = data[1], data[2], data[3], data[4]
    btn = product(product_id)
    await call.message.edit_text(f'{product_name}\n\n'
                                 f'{product_desc}\n\n'
                                 f'Narxi: {product_price}', reply_markup=btn)
