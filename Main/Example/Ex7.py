# Необходимо написать программу, которая будет считывать со стандартного ввода строку.
# Нужно разбить строку на слова, словом будем считать последовательность
# символов отличных от пробелов (то есть знаки пунктуации будут входить в слова).
# Далее нужно посчитать и вывести среднее число символов в словах этого текста.
# Точность проверяется до 2го знака после запятой (точность +-0.01).
# * Решение можно реализовать в 2 строки кода.

# strings = "Sums start and the items of an iterable from left to right and returns the total."

# strings = input().split()
# l = 0.0
# for x in strings:
#     l += len(x)
# l = l / len(strings)
# print(l)

# strings = input()
# print(sum(len(x) for x in strings.split())/len(strings.split()))
# на 12ом тесте выдает ошибку

s = input().split()
print(sum(len(x) for x in s)/len(s) if s else 0.00)