from aiogram.types import CallbackQuery

from keyboards.inline.inline_menu import show_card_btn, main_menu
from loader import dp, db
from aiogram.dispatcher import FSMContext


@dp.callback_query_handler(text=['remove_' + str(i) for i in range(1, 101)])
async def remove(call: CallbackQuery, state: FSMContext):
    product_id = call.data.split('remove_')[1]
    data = await state.get_data()
    await state.finish()
    product_data = await db.get_product_by_id(product_id)
    product_name = product_data[1]
    del data[product_name]
    if data:
        await state.update_data(data)
        result = ''
        for key, inner_key in data.items():
            result += f'{key}\n\n' \
                      f'Narxi: {inner_key["price"]} ✖ {inner_key["quantity"]} = {inner_key["total"]}\n' \
                      f'{"-" * 25}'

        await call.answer()
        btn = await show_card_btn(data)
        await call.message.edit_text(result, reply_markup=btn)
    else:
        btn = main_menu
        await call.message.edit_text(f"Bo'limlardan birini tanlang: ", reply_markup=btn)
        await call.answer("Savat bo'sh❗")


