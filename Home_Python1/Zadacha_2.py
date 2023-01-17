# 2.	Создайте программу для игры в 'Крестики-нолики'
# НЕОБЯЗАТЕЛЬНО Добавить игру против бота с интеллектом

from random import randint as RA


def board(my_list):
    print('-------------')
    for i in range(3):
        print('|', my_list[0 + i * 3], '|', my_list[1 + i * 3], '|', my_list[2 + i * 3], '|')
        print('-------------')


def human(my_list):
    enter_hod = input('Выберите ячейку: ')
    try:
        enter_hod = int(enter_hod)
    except:
        print('Ввод не корректен! Выберите ячейку. ')
        return human(my_list)
    if 1 > enter_hod > 9:
        print('Ввод не корректен! Выберите число от 1 до 9.')
        return human(my_list)
    if str(my_list[enter_hod - 1]) not in 'XO':
        my_list[enter_hod - 1] = 'X'
    else:
        print('Ошибка, ячейка заполнена. Выберите другую ячейку.')
        return human(my_list)
    return my_list


def bot(my_list):
    tuple_victory = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for j in tuple_victory:
        for i in tuple_victory:
            if my_list[i[0]] == my_list[i[1]] == 'O' and str(my_list[i[2]]) not in 'XO':
                my_list[i[2]] = 'O'
                print(f'Ход бота {i[2] + 1}')
                return my_list
                break
            elif my_list[i[1]] == my_list[i[2]] == 'O' and str(my_list[i[0]]) not in 'XO':
                my_list[i[0]] = 'O'
                print(f'Ход бота {i[0] + 1}')
                return my_list
                break
            elif my_list[i[0]] == my_list[i[2]] == 'O' and str(my_list[i[1]]) not in 'XO':
                my_list[i[1]] = 'O'
                print(f'Ход бота {i[1] + 1}')
                return my_list
                break
        if my_list[j[0]] == my_list[j[1]] and str(my_list[j[2]]) not in 'XO':
            my_list[j[2]] = 'O'
            print(f'Ход бота {j[2] + 1}')
            return my_list
            break
        if my_list[j[1]] == my_list[j[2]] and str(my_list[j[0]]) not in 'XO':
            my_list[j[0]] = 'O'
            print(f'Ход бота {j[0] + 1}')
            return my_list
            break
        if my_list[j[0]] == my_list[j[2]] and str(my_list[j[1]]) not in 'XO':
            my_list[j[1]] = 'O'
            print(f'Ход бота {j[1] + 1}')
            return my_list
            break
    enter_hod = RA(0, 8)
    if str(my_list[enter_hod]) not in 'XO':
        my_list[enter_hod] = 'O'
    else:
        return bot(my_list)
    print(f'Ход бота {enter_hod+1}')
    return my_list


def control_win(my_list):
    tuple_hod = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for i in tuple_hod:
        if my_list[i[0]] == my_list[i[1]] == my_list[i[2]]:
            return my_list[i[0]]


def main_game(my_list):
    board(my_list)
    num = RA(1, 2)
    if num == 1:
        for i in range(len(my_list)):
            my_list = human(my_list)
            board(my_list)
            if i == 4:
                print('Ничья!')
                break
            if i > 1:
                hod = control_win(my_list)
                if hod:
                    print(f'{hod} победил!!!')
                    break
            my_list = bot(my_list)
            board(my_list)
            if i > 1:
                hod = control_win(my_list)
                if hod:
                    print(f'{hod} победил!!!')
                    break
    if num == 2:
        for i in range(len(my_list)):
            my_list = bot(my_list)
            board(my_list)
            if i > 1:
                hod = control_win(my_list)
                if hod:
                    print(f'{hod} победил!!!')
                    break
            if i == 4:
                print('Ничья!')
                break
            my_list = human(my_list)
            board(my_list)
            if i > 1:
                hod = control_win(my_list)
                if hod:
                    print(f'{hod} победил!!!')
                    break


new_list = [i for i in range(1, 10)]
main_game(new_list)
