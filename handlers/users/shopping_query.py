from aiogram.types import CallbackQuery, ShippingQuery
from aiogram.dispatcher import FSMContext
from shopping_config.product_invoice import generate_product_invoice, EXPRESS_SHIPPING, REGULAR_SHIPPING, \
    PICKUP_SHIPPING, REGIONS_SHIPPING

from loader import dp, bot


@dp.callback_query_handler(text='order')
async def send_product_invoice(call: CallbackQuery, state: FSMContext):
    chat_id = call.from_user.id
    product_data = await state.get_data()
    if product_data:
        await bot.send_invoice(chat_id=chat_id, **generate_product_invoice(product_data).generate_invoice(),
                               payload='shopbot')
    else:
        await call.answer("Savat bo'sh❗")
