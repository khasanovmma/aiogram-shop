from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from keyboards.inline.inline_menu import show_card_btn
from loader import dp, db


@dp.callback_query_handler(text=['show_card', 'shopping_card'])
async def show_product_card(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    if data:
        result = ''
        for key, inner_key in data.items():
            result += f'<b>{key}</b>\n\n' \
                     f'<i>Narxi: {inner_key["price"]} ✖ {inner_key["quantity"]} = {inner_key["total"]}\n</i>' \
                      f'<b>{"-" * 46}</b>'
        await call.answer()
        btn = await show_card_btn(data)
        await call.message.edit_text(result, reply_markup=btn)
    else:
        await call.answer("Savat bo'sh❗")



