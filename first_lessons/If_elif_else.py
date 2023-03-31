# Задание №1

t = int(input("введите температуру: "))

if t > 10:
	print("хорошая погода")
else:
	print("плохая погода")

# Задача №2

p = int(input("твоя оценка: "))

if p == 5:
	print("Молодец!")
elif p == 4:
	print("Хорошо!")
elif p <= 3:
	print("Лентяй!")

# Задача №1

number = int(input("введите число: "))

if number%4==0 & number%2==0:
	print("да")
else:
	print("нет")


# Задача №2

number = int(input("введите число: "))

if number%5==0 and number%2!=0:
	print("да")
else:
	print("нет")

# Задача №3

number = int(input("введите число: "))

if number%7==0 and number%2!=0:
	print("да")
else:
	print("нет")

# Задача №4

number = int(input("введите число: "))

if number%10==0 and number%2==0:
	print("да")
else:
	print("нет")


# Задача №5

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

m = int(input("m = "))
k = int(input("k = "))

if ((a <= k and b <= k) 
	or (b <= k and c <= k)
    or (a <= k and c <= k)):
    print("yes")
else:
    print("no")


# Задача №6

number = float(input("число: "))

if number > 0:
    print("положительное")
elif number < 0:
    print("отрицательное")
else:
    print("ноль")


# Задача №7
import math

D = int(input("диаметр бревна = "))
A = math.sqrt(int(input("ширина бруса = ")))

if A <= D:
    print("можно")
else:
    print("нельзя")


# Задача №8

S = int(input("площадь зала = "))
R = int(input("радиус сцены = "))
K = int(input("проход от стены не менее = "))

if (S - R) >= K:
    print("норм")
else:
    print("не")



# Задача №9

number = int(input("ваш номер = "))

if number <= 54:
    if number < 37:
        print("купе")
    else:
        print("боковое")
    if number%2==0:
        print("верхнее место")
    else:
        print("нижнее место")
else:
    print("нет такого места")


# Задача №10

money = int(input("сколько у вас? "))

if(money%500==0):
    print(money//500, "купюры по 500")
if(money%100==0):
    print(money//100, "купюры по 100")
if(money%10==0):
    print(money//10, "монет по 10")
if(money%2==0):
    print(money//2, "монет по 2")

# Задача №10 2 способ

money = int(input("сколько у вас? "))

naminal500 = money//500
money = money%500

naminal100 = money//100
money = money%100

naminal10 = money//10
money = money%10

naminal2 = money//2
money = money%2

print(naminal500,"по 500\t", naminal100,"по 100\t", naminal10,"по 10\t", naminal2 ,"по 2\t",)


# Задача №11,12
import math
A = int(input("ребро куба: "))

H = int(input("высота цилиндра: "))
R = int(input("радиус цилиндра: "))

M = int(input("объем жидкости"))

if A ** 3 + math.pi * R**2 * H <= M:
    print("жидкость заполнит оба сосуда")
if A ** 3 <= M:
    print("жидкость заполнит кубический сосуд")
if math.pi * R**2 * H <= M:
    print("жидкость заполнит цилиндрический сосуд")
    

# Задача №13 

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

if ((a <= b + c) 
	and (b <= a + c)
    and (c <= a + b)):
    print("существует")
    if c**2 == a**2 + b**2:
        print("он прямоугольный")
else:
    print("не существует")

#задача 14
a = int(input("a = "))
b = int(input("b = "))
x = int(input("x = "))
print(a <= x <= b)


#задача 16 
A = int(input("A = "))
B = int(input("B = "))
C = int(input("C = "))

if A < B < C:
    print("A < B < C")
if A > B >= C:
    print("A > B >= C")

