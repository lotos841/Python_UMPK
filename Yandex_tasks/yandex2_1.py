
#A
print("Привет, Яндекс!")


#B
username = input("Как Вас зовут?")
print("Привет,", username)


#C
info = input()
print(info)
print(info)
print(info)



#D
money = int(input())
money = money - 2.5 * 38
print(int(money))


#E
price = int(input())
weight = int(input())
money = int(input())
money = money - weight * price
print(int(money))


#F
product = input()
price = int(input())
weight = int(input())
money = int(input())

print("Чек")
print(f"{product} - {weight}кг - {price}руб/кг")
print(f"Итого: {price * weight}руб")
print(f"Внесено: {money}руб")
print(f"Сдача: {money - price * weight}руб")


#G
count = int(input())

print("Купи слона!\n" * count)


#H
count = int(input())
phrase = input()
print(f'Я больше никогда не буду писать "{phrase}"!\n' * count)


#I
print(int(input()) // 2 * int(input()))


#J
name = input()
number = int(input())

print(f"Группа №{str(number)[0]}.")
print(f"{str(number)[2]}. {name}.")
print(f"Шкафчик: {number}.")
print(f"Кроватка: {str(number)[1]}.")


#K
n = input()
print(n[1] + n[0] + n[3] + n[2])


#L
num1 = int(input())
num2 = int(input())

result_num1 = ((num1 % 10) + (num2 % 10)) % 10
result_num2 = ((num1 // 10 % 10) + (num2 // 10 % 10)) % 10
result_num3 = ((num1 // 100) + (num2 // 100)) % 10

print(f'{result_num3}{result_num2}{result_num1}')


#M
n = int(input())
m = int(input())
c = m // n
d = m % c
print(c)
print(d)


#N
red = int(input())
green = int(input())
blue = int(input())

print((red + blue) + 1)


#O
N = int(input())
M = int(input()) 
T = int(input()) 
hours = (T % (60 * 24) // 60)
minutes = (T % 60)
thours = (((hours + N) + (minutes + M) // 60) % 24)
tminutes = ((minutes + M) % 60)
print(f'{thours:02}:{tminutes:02}')


#P
A = int(input())
B = int(input())
C = int(input())

time1 = ((B - A) / C * 100) // 100
time2 = ((B - A) / C * 100) % 100

time = time1 + (time2 / 100)
print(format(time, '.2f'))


#Q
a = int(input())
b = int(input())
 
oldb = b
newb = n = 0
while oldb:
    newb += oldb % 10 * 2 ** n
    oldb //= 10
    n += 1
 
out = a + newb
print(out)


#R
price = input()
naminal = int(input())
 
print(naminal - int(price, 2))


#S
product = input()
price = int(input())
weight = int(input())
money = int(input())
check = 'Чек'
result_price = f"{weight}кг * {price}руб/кг"
total = f'{price * weight}руб'
enter_money = f'{money}руб'
change = f'{money - price * weight}руб'
 
print(f'{check:^35}'.replace(' ', '='))
print(f'Товар: {product.rjust(35 - 7)}')
print(f'Цена:{result_price.rjust(35 - 5)}')
print(f'Итого:{total.rjust(35 - 6)}')
print(f'Внесено: {enter_money.rjust(35 - 9)}')
print(f'Сдача: {change.rjust(35 - 7)}')
print('=' * 35)


#T
N = int(input())
M = int(input())
K1 = int(input())  
K2 = int(input())  

weight1 = (M * N - N * K2) / (K1 - K2)
weight2 = N - weight1
print(int(weight1), int(weight2), sep=' ')