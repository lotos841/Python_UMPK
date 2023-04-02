

#A
while (childs_screams := input()) != "Три!":
    print("Режим ожидания...")
print("Ёлочка, гори!")


#B
key_value = "зайка"
bunny_find_count = 0

while (phrase := input()) != "Приехали!":
    if key_value in phrase:
        bunny_find_count += 1
print(bunny_find_count)


#C
for i in range(int(input()), int(input()) + 1):
    print(i, end=" ")


#D
n = int(input())
k = int(input())
step = 1

if n > k:
    step = -1

for i in range(n, k + step, step):
    print(i, end=" ")


#E
sum = 0

while (product_price := float(input())) != 0:
    if product_price >= 500:
        sum += product_price - product_price * 10 / 100
    else:
        sum += product_price
print(sum)


#F
num1 = int(input())
num2 = int(input())

while num1 != num2:
    if num1 > num2:
        num1 -= num2
    else:
        num2 -= num1
print(num1)


#G
a = int(input())
b = int(input())

i = min(a, b)
while True:
    if i % a == 0 and i % b == 0:
        break
    i += 1
print(i)


#H
info = input()

for i in range(int(input())):
    print(info)


#I
num = int(input())

result = 1
for i in range(1, num + 1):
    result *= i
print(result)


#J
pos_y = 0
pos_x = 0

while (direction := input()) != "СТОП":
    match direction:
        case "СЕВЕР":
            pos_y += int(input())
        case "ЮГ":
            pos_y -= int(input())
        case "ЗАПАД":
            pos_x -= int(input())
        case "ВОСТОК":
            pos_x += int(input())
print(pos_y)
print(pos_x)


#K
num = int(input())
sum = 0
for i in range(len(str(num))):
    sum += int(str(num)[i])
print(sum)


#L
num = int(input())
max_figure = 0
for i in range(len(str(num))):
    if max_figure < int(str(num)[i]):
        max_figure = int(str(num)[i])
print(max_figure)


#M
player_count = int(input())
min_name = "ввввввввв"

for i in range(player_count):
    player_name = input()
    if player_name < min_name:
        min_name = player_name
print(min_name)


#N
num = int(input())

if num > 1:
    for i in range(2, int(num / 2) + 1):
        if (num % i) == 0:
            print("NO")
            break
    else:
        print("YES")
else:
    print("NO")


#O
phrase_count = int(input())
key_value = "зайка"
bunny_find_count = 0

for i in range(phrase_count):
    phrase = input()
    if key_value in phrase:
        bunny_find_count += 1
print(bunny_find_count)


#P
num = int(input())
result = "NO"

for i in range(int(len(str(num)) / 2)):
    if int(str(num)[i]) == int(str(num)[-i - 1]):
        result = "YES"
    else:
        result = "NO"
        break
print(result)


#Q
num = int(input())
new_num = ""

for i in range(int(len(str(num)))):
    if int(str(num)[i]) % 2 != 0:
        new_num += str(num)[i]
print(new_num)


#R Пока нэт решэнэй!


#S
min_gues = 1
max_gues = 1000
mid_gues = (min_gues + max_gues) // 2
print(mid_gues)
answer = input()

while 'Угадал!' not in answer:
    if 'Меньше' in answer:
        max_gues = mid_gues - 1
    elif 'Больше' in answer:
        min_gues = mid_gues + 1
    mid_gues = (min_gues + max_gues) // 2
    print(mid_gues)
    answer = input()


#T
blocks_count = int(input())
p = 0
bad = - 1
for i in range(blocks_count):
    block = int(input())
    h, r, m = block % 256, (block // 256) % 256, block // 256 ** 2
    t = ((m + r + p) * 37) % 256
    if t != h or h >= 100:
        bad = i
        break
    p = h
print(bad)