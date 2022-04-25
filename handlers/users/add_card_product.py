from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from loader import dp, db


@dp.callback_query_handler(text='add_product')
async def add_product(call: CallbackQuery, state: FSMContext):
    quantity = int(call.message.reply_markup.inline_keyboard[0][1].text)
    product_id = call.message.reply_markup.inline_keyboard[2][0].callback_data.split('back_product_list_')[1]
    data = await db.get_product_by_id(product_id)
    product_name, product_price = data[1], int(float(data[-1]))
    await state.update_data({
        product_name: {
            'price': product_price,
            'quantity': quantity,
            'total': product_price * quantity,
            'product_id': product_id
        }
    })
    await call.answer("Mahsulot qo'shildi")
