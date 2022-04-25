from aiogram.dispatcher.filters import Command
from aiogram.types import Message

from filters import IsPrivate
from loader import dp


@dp.message_handler(Command('update'), IsPrivate(), state=None)
async def start_register(msg: Message):
    await msg.answer('Uy ishi')