# 3.	Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# aaaaabbbcccc -> 5a3b4c
# 5a3b4c -> aaaaabbbcccc

def compression(my_list, text):
    count = 1
    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            my_list.append(str(count) + text[i - 1])
            count = 1
    my_list.append(str(count) + text[i - 1])
    a = ''.join(my_list)
    return a

def expand(text):
    second_list = []
    size = len(text)
    i = 0
    while i < size:
        test = ''
        t = text[i]
        while '0' <= t <= '9':
            test += t
            i += 1
            if i < size:
                t = text[i]
            else:
                break
        if test != '':
            e = int(test)
        el = text[i]
        for p in range(e):
            second_list.append(el)
        i += 1
    second_list = ''.join(second_list)
    return second_list

line = 'aaaaabbbcccc'
new_list = []
comp = compression(new_list, line)
print(comp)
print(expand(comp))
