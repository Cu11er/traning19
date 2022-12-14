# Мы продолжаем пробовать себя в качестве разработчика игр. Теперь нужно написать небольшую логику поведения некоторых отрядов,
# а также их урон. Есть два отряда, в каждом по 10 монстров. В первом отряде у каждого монстра урон абсолютно случайный
# и колеблется от 50 до 80, а во втором — от 30 до 60. Оба отряда вместе напали на третий, также из 10 юнитов.
# Юнит третьего отряда погибает, если сумма урона от двух монстров больше 100.
#
# Напишите программу, которая генерирует случайные значения в первых двух списках в заданных диапазонах,
# а также генерирует список, состоящий из фраз «Погиб» или «Выжил». Выведите все списки на экран.
#
# Пример:
#
# Урон первого отряда: [77, 75, 76, 77, 76, 73, 57, 67, 76, 52]
# Урон второго отряда: [53, 51, 31, 60, 49, 37, 31, 60, 37, 47]
# Состояние третьего отряда: ['Погиб', 'Погиб', 'Погиб', 'Погиб', 'Погиб', 'Погиб', 'Выжил', 'Погиб', 'Погиб', 'Выжил']

import random

units_1 = [random.randint(50, 80) for _ in range(10)]
units_2 = [random.randint(30, 60) for _ in range(10)]
units_3_condition = [('Погиб' if units_1[i_damage] + units_2[i_damage] > 100
                      else 'Выжил')
                     for i_damage in range(10)]


print('Урон первого отряда:', units_1)
print('Урон Второго отряда:', units_2)
print('Состояние третьего отряда:', units_3_condition)