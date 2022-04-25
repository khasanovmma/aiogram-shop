from aiogram.types import CallbackQuery

from keyboards.inline.inline_menu import product
from loader import dp, db


@dp.callback_query_handler(text='plus')
async def product_add(call: CallbackQuery):
    quantity = int(call.message.reply_markup.inline_keyboard[0][1].text)
    product_id = call.message.reply_markup.inline_keyboard[2][0].callback_data.split('back_product_list_')[1]
    quantity += 1
    btn = await product(product_id, str(quantity))
    await call.message.edit_reply_markup(reply_markup=btn)
    await call.answer(cache_time=1)


@dp.callback_query_handler(text='minus')
async def product_add(call: CallbackQuery):
    quantity = int(call.message.reply_markup.inline_keyboard[0][1].text)
    product_id = call.message.reply_markup.inline_keyboard[2][0].callback_data.split('back_product_list_')[1]
    if quantity > 1:
        quantity -= 1
        btn = await product(product_id, str(quantity))
        await call.message.edit_reply_markup(reply_markup=btn)
        await call.answer(cache_time=1)
    else:
        await call.answer(text="Minumum qiymatga yetib keldingiz ❗",
                          show_alert=True)


@dp.callback_query_handler(text='quantity')
async def product_quantity(call: CallbackQuery):
    await call.answer()