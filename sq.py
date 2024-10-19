"""
Напишите программу sq.py, которая получает из первого аргумента командной строки последовательность целых чисел, а затем выводит на экран:

1 – если передана строго возрастающая последовательность целых чисел;
0 – если последовательность не возрастающая (убывающая или содержащая два одинаковых элемента рядом).
Пример запуска программы:
> python sq.py '1 2 3 5'
1

"""
import sys
# Получаем строку, приводим к виду списка без пробелов
sq = sys.argv[1].strip().split(' ')

# Сортировка чисел по возрастанию
sq_sorted = sorted(sq, key=int)


# Определяем, если есть повторяющиеся значения или нарушение порядка возрастания, то возвращаем 0
if len(sq) > len(set(sq)) or not sq_sorted == sq:
    print(0)
else:
    print(1)
