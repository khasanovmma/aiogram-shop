from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def main_menu(data_list, subcategory=False, product=False, product_subcategory_code=None):
    menu = InlineKeyboardMarkup(row_width=1)
    for inner_data in data_list:
        menu.insert(InlineKeyboardButton(text=inner_data[0], callback_data=inner_data[1]))

    if subcategory:
        menu.insert(InlineKeyboardButton(text='🔙 Ortga', callback_data='back_category'))
    elif product:
        menu.insert(InlineKeyboardButton(text='🔙 Ortga', callback_data='back_' + product_subcategory_code))

    return menu


def product(product_id, quantity=None):
    menu = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='➖', callback_data='minus'),
            InlineKeyboardButton(text='1' if not quantity else quantity, callback_data='quantity'),
            InlineKeyboardButton(text='➕', callback_data='plus')
        ],
        [
            InlineKeyboardButton(text="Savatni ko'rish 🛒", callback_data='show_card'),
            InlineKeyboardButton(text="Savatga qo'shish 🛍", callback_data='add_product')
        ],
        [
            InlineKeyboardButton(text='🔙 Ortga', callback_data='back_product_list_' + product_id)
        ]
    ])

    return menu


def show_card_btn(product_data):
    menu = InlineKeyboardMarkup(
        inline_keyboard=[

            [
                InlineKeyboardButton(text='🔙 Bosh menu', callback_data='back_category'),
                InlineKeyboardButton(text='Savatni tozalash', callback_data='clear'),
            ],
            [
                InlineKeyboardButton(text=f'❌ {key}', callback_data=f'remove_{product_data[key]["product_id"]}') for key
                in product_data
            ],
            [
                InlineKeyboardButton(text='Buyurtma berish 🛍', callback_data='order')
            ]
        ]
    )
    return menu
