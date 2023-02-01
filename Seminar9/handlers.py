from loader import dp, bot
from aiogram import types
import time
from random import randint

total = 0


@dp.message_handler(commands=['start'])
async def mes_start(message: types.Message):
    await message.answer(f'Привет {message.from_user.first_name}! \nРад тебя видеть! \nСыграем в  игру "Candy-candy"? '
                         f'\nЕсли готов начать введи на клавиатуре "/DA и укажи общее количество конфет в тарелке, но '
                         f'помни количество конфет изначально не может быть меньше 29. "\n(пример: /DA количество конфет)')

@dp.message_handler(commands=['DA'])
async def mes_start2(message: types.Message):
    global total
    count = message.text.split()[1]
    total = int(count)
    await message.answer(f'В тарелке находится: {total} конфет')
    time.sleep(1)
    await message.answer('Чтож, преступим!!! Правила игры следующие: \n1.Быть милашкой)). Шутка!! \n2. За  один ход'
                         ' нельзя взять больше чем 28 конфет.'
                         '\n3. Кто из нас ходит первый: опеределяется случайной жеребьевкой. '
                         '\n4. Победу одержит тот, кто сделал последний ход.'
                         '\n Желаю удачи, друг! :)')
    time.sleep(1)
    await message.answer(f'Спасибо что ты ознакомился с правилами. Игра начинается!!!')
    time.sleep(1)
    first_player = 1
    second_player = 2
    draw = randint(1, 2)
    if draw == first_player:
        await message.answer(f'По результатам жеребьевки. Ход первый за тобой {message.from_user.first_name} Выбери '
                             f'количество конфет которое ты хочешь взять из тарелки?')
    if draw == second_player:
        await message.answer(f'Увы не повезло! По результатам жеребьевки. Первым хожу я!!')
        time.sleep(1)
        second_player_ch = randint(1, 28)
        if total <= 28:
            second_player_ch = total
        if total <= 57 and total >= 30:
            second_player_ch = total - 29
        await message.answer(f'Я забираю из тарелки {second_player_ch} конфет')
        total -= second_player_ch
        await message.answer(f'Конфет в тарелке осталось - {total}')
        await message.answer(f'Теперь дружок {message.from_user.first_name} твой ход!')


@dp.message_handler()
async def mes_all(message: types.Message, updater=None):
    global total
    if message.text.isdigit() and int(message.text) > 0 and int(message.text) < 29 and int(message.text) <= total:
        first_player_ch = int(message.text)
        total -= first_player_ch
        await bot.send_message(message.from_user.id, f'Конфет в тарелке осталось - {total}')
        if total == 0:
            await bot.send_message(message.from_user.id, f'Поздравляю. Вы ПОБЕДИТЕЛЬ!')
            updater.stop()
        time.sleep(1)
        second_player_ch = randint(1, 28)
        if total <= 28:
            second_player_ch = total
        if total <= 57 and total >= 30:
            second_player_ch = total - 29
        await message.answer(f'Я забираю из тарелки {second_player_ch} конфет')
        total -= second_player_ch
        await message.answer(f'Конфет в тарелке - {total}')
        if total == 0:
            await bot.send_message(message.from_user.id, f'Ура!! Я ПОБЕДИЛ!! Не грусти, у тебя всё получится.')
            updater.stop()
    else:
        await bot.send_message(message.from_user.id, 'Пожалуйста введите правильное значение')