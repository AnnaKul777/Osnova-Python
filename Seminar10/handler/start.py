import game
from loader import dp
from aiogram.types import Message


@dp.message_handler(commands=['start'])
async def mes_start(message: Message):
    for duel in game.total:
        if message.from_user.id == duel[0]:
            await message.answer('Ты уже начал игру! Играй давай!')
            break
    else:
        await message.answer(f'Привет, {message.from_user.full_name}. '
                             f'Мы будем играть в конфеты.')
        await message.answer(
            f'По умолчанию количество конфет, лежащих на столе определено в размере 150. Если тебя это устраивает кликни на /DA'
            f'\nЕсли не устраивает, ты можешь сам выбрать количество конфет, для этого введи /ch (количество конфет). '
            f'Количество вводится через пробел')
