from aiogram.dispatcher.filters import Command
from aiogram.types import Message

from loader import dp


@dp.message_handler(Command('update'), state=None)
async def start_register(msg: Message):
    await msg.answer('Uy ishi')