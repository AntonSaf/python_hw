'''
Задача 1:
Напишите программу, которая решает квадратные уравнения даже если дискриминант отрицательный.
Используйте комплексные числа для извлечения квадратного корня.
'''

#a = 6
#b = -4
#c = 3

a = float(input("Введите А = "))
b = float(input("Введите B = "))
c = float(input("Введите C = "))

D = complex(b**2 - 4*a*c, 0)
x1 = (-b + D**0.5)/(2*a)
x2 = (-b - D**0.5)/(2*a)
print(D, x1, x2)
