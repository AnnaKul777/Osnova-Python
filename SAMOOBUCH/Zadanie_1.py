
# iterable = [1, 5, 7]
# for a in iterable:
#     print(a)

#FOR________________________________________

# pets = ['cats', 'dog', 'rabbits', 'hamsters']
# # for myPets in pets:
# #     print(myPets)
# for index, myPets in enumerate(pets):  # вывести индекс со значением элементов
#     print(index, myPets)

# age = {'Peter': 5, 'John': 7}
# # for i in age:
# #     print(i)
# for i in age:
#     print('Name = %s, Age = %d' %(i, age[i]))

# age = {'Peter': 5, 'John': 7}
# for i,j in age.items():                           #возвращает ввиде кортежа (значение + ключ)
#     print('Name = %s, Age = %d' %(i, j))

# massage = 'Hello'
# for i in massage:
#     print(i)

# for i in range(5):                   #перебор чисел
#     print(i)

# WHILE___________________________________________________
# counter = 5
# while counter > 0:
#     print('Counter =', counter)
#     counter = counter -1                                # обязательно условия для прерывания цикла указать

# BREAK
# j = 0
# for i in range(5):  # if может использоваться в цикле for, while внутри if, for  внутри while
#     j = j + 2
#     print('i = ', i, ', j = ', j)
#     if j == 6:
#         break

#CONTINUE
# j = 0
# for i in range(5):
#     j = j +2
#     print('\ni = ', i, ', j = ', j)
#     if j == 6:
#         continue
#     print('Я буду пропущен, если j = 6')

#TRY/EXCEPT
# try что то сделать
# except сделать что то другое в случае ошибки
# try:
#     answer =12/0
#     print(answer)
# except:
#     print('An error ossurred (Произошла ошибка)')

# try:
#     userInput1 = int(input('Please enter a number: '))
#     userInput2 = int(input('Please enter another number: '))
#     answer = userInput1 / userInput2
#     print('The answer is', answer)
#     myFile = open('missing.txt', 'r')
# except ValueError:                              # при введении строки и когда невозможно преобразовать в целое число
#     print('Error: You did not enter a number')
# except ZeroDivisionError:                   # при деления на 0
#     print('Error: Cannot divide by zero')
# except Exception as e:
#     print('Unknown error: ', e)

 # ФУНКЦИИ

# newString = 'Hello world'.replace('world', 'Universe')
# print(newString)

def checkPrime(numberToCheck):
    for x in range(2, numberToCheck):
        if (numberToCheck % x == 0):
            return False
        return True
