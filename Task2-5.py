# Реализуйте алгоритм перемешивания списка

# Задача 2-4 натолкнула на мысль использовать рандомное перемешивание
# используем библиотеку псевдорандома
import random

# заводим списки nabor1=исходный, nabor2=искомый
nabor1 = [5, 8, -1, 12, 0, 3, 11, -6, 1]
nabor2 = []

# выводим исходный список на экран
print(nabor1)
# инициализируем 2 переменные для рандомных индексов
randNumber1 = randNumber2 = 0

# пока список больше, чем из 1 элемента идем цикл
while len(nabor1)>1:
    # проверяем, что рандомные числа неодинаковые
    while randNumber1 == randNumber2:
        randNumber1 = random.randint(0, len(nabor1)-1)
        randNumber2 = random.randint(0, len(nabor1)-1)
    # добавляем в новый список числа с получившихся рандомных позиций
    nabor2.append(nabor1[randNumber1])
    nabor2.append(nabor1[randNumber2])
    # удаляем из исходного списка элементы с этих рандомных индексов 
    # (сначала с большего индекса, потом с меньшего)
    if randNumber1 > randNumber2:
        nabor1.pop(randNumber1)
        nabor1.pop(randNumber2)
    else:
        nabor1.pop(randNumber2)
        nabor1.pop(randNumber1)
    
    # принудительно делаем рандомные числа одинаковыми, чтобы сгенерировались новые
    randNumber1 = randNumber2 = 0

# если количество элементов списка было нечетным, то один элемент останется
# добавим его в искомый
if len(nabor1) == 1:
    nabor2.append(nabor1[0])

# выводим искомый список
print(nabor2)