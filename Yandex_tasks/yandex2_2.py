

#A
print("Как Вас зовут?")
user_name = input()
print(f"Здравствуйте, {user_name}!")

print("Как дела?")
user_mood = input()
if user_mood == "хорошо":
    print("Я за вас рада!")
elif user_mood == "плохо":
    print("Всё наладится!")


#B
Petya_speed = int(input())
Vasya_speed = int(input())

if Petya_speed > Vasya_speed:
    print("Петя")
else:
    print("Вася")


#C
Petya_speed = int(input())
Vasya_speed = int(input())
Tolya_speed = int(input())

if Petya_speed > Vasya_speed and Petya_speed > Tolya_speed:
    print("Петя")
elif Vasya_speed > Petya_speed and Vasya_speed > Tolya_speed:
    print("Вася")
else:
    print("Толя")


#D
Petya_speed = int(input())
Vasya_speed = int(input())
Tolya_speed = int(input())

if Petya_speed > Vasya_speed and Petya_speed > Tolya_speed:
    if Vasya_speed > Tolya_speed:
        print("1. Петя")
        print("2. Вася")
        print("3. Толя")
    else:
        print("1. Петя")
        print("2. Толя")
        print("3. Вася")
elif Vasya_speed > Petya_speed and Vasya_speed > Tolya_speed:
    if Petya_speed > Tolya_speed:
        print("1. Вася")
        print("2. Петя")
        print("3. Толя")
    else:
        print("1. Вася")
        print("2. Толя")
        print("3. Петя")
elif Tolya_speed > Petya_speed and Tolya_speed > Vasya_speed:
    if Petya_speed > Vasya_speed:
        print("1. Толя")
        print("2. Петя")
        print("3. Вася")
    else:
        print("1. Толя")
        print("2. Вася")
        print("3. Петя")


#E
Petya_apple_count = 6
Vasya_apple_count = 9

N = int(input())
M = int(input())

Petya_apple_count += N
Vasya_apple_count += M

if Petya_apple_count > Vasya_apple_count:
    print("Петя")
else:
    print("Вася")


#F
year = int(input())

if year % 4 != 0:
    print("NO")
elif year % 100 != 0:
    print("YES")
elif year % 400 == 0:
    print("YES")
else:
    print("NO")

#G
num = int(input())
 
if num // 1000 % 10 == num % 10 and num // 100 % 10 == num // 10 % 10: 
    print("YES") 
else: 
    print("NO")


#H
massage = input()
if "зайка" in massage:
    print("YES")
else:
    print("NO")


#I
name1 = input()
name2 = input()
name3 = input()

toss_result = min(name1,name2,name3)
print(toss_result)


#J
old_pass = int(input())

num1 = old_pass % 10 + old_pass // 10 % 10
num2 = old_pass //100 % 10 + old_pass // 10 % 10
if num2 > num1:
    print(str(num2) + str(num1))
else:
    print(str(num1) + str(num2))


#K
enter_num = int(input())
figure1 = enter_num // 100
figure2 = (enter_num - (figure1 * 100)) // 10
figure3 = (enter_num - (figure1 * 100) - (figure2 * 10))
if figure1 > figure2:
    figure1, figure2 = figure2, figure1
if figure2 > figure3:
    figure2, figure3 = figure3, figure2
if figure1 > figure2:
    figure1, figure2 = figure2, figure1
if figure2 > figure3:
    figure2, figure3 = figure3, figure2
if figure1 > figure2:
    figure1, figure2 = figure2, figure1
if (figure1 + figure3) / 2 == figure2:
    print('YES')
else:
    print('NO')


#L
a = int(input())
b = int(input())
c = int(input())

if ((a < b + c) and (b < a + c) and (c < a + b)):
    print("YES")
else:
    print("NO")


#M
eLf_num = int(input())
gnom_num = int(input())
people_num = int(input())

if eLf_num % 10 == gnom_num % 10 == people_num % 10:
    print(eLf_num % 10)
elif eLf_num // 10 % 10 == gnom_num // 10 % 10 == people_num // 10 % 10:
    print(eLf_num // 10 % 10)


#N
number = int(input())
figure1 = number // 100
figure2 = number // 10 % 10
figure3 = number % 10

max_number = max(figure1, figure2, figure3)
min_number = min(figure1, figure2, figure3)
sr = (figure1 + figure2 + figure3) - max_number - min_number
if min_number == 0:
    print(f"{sr}{min_number} {max_number}{sr}")
else:
    print(f"{min_number}{sr} {max_number}{sr}")


#O
num1 = int(input())
figure1_num1 = num1 // 10
figure2_num1 = num1 % 10
num2 = int(input())
figure1_num2 = num2 // 10
figure2_num2 = num2 % 10
 
if figure1_num1 > figure2_num1:
    figure1_num1, figure2_num1 = figure2_num1, figure1_num1
if figure1_num2 > figure2_num2:
    figure1_num2, figure2_num2 = figure2_num2, figure1_num2
if figure1_num1 > figure1_num2:
    figure1_num1, figure1_num2 = figure1_num2, figure1_num1
if figure2_num1 > figure2_num2:
    figure2_num1, figure2_num2 = figure2_num2, figure2_num1
if figure2_num1 > figure1_num2:
    figure1_num2, figure2_num1 = figure2_num1, figure1_num2
print(figure2_num2 * 100 + (figure1_num2 + figure2_num1) % 10 * 10 + figure1_num1)


#P
Petya_speed = int(input())
Vasya_speed = int(input())
Tolya_speed = int(input())

if Petya_speed > Vasya_speed and Petya_speed > Tolya_speed:
    if Vasya_speed > Tolya_speed:
        print("          Петя          ")
        print("  Вася                  ")
        print("                  Толя  ")
        print("   II      I      III   ")
    else:
        print("          Петя          ")
        print("  Толя                  ")
        print("                  Вася  ")
        print("   II      I      III   ")
elif Vasya_speed > Petya_speed and Vasya_speed > Tolya_speed:
    if Petya_speed > Tolya_speed:
        print("          Вася          ")
        print("  Петя                  ")
        print("                  Толя  ")
        print("   II      I      III   ")
    else:
        print("          Вася          ")
        print("  Толя                  ")
        print("                  Петя  ")
        print("   II      I      III   ")
elif Tolya_speed > Petya_speed and Tolya_speed > Vasya_speed:
    if Petya_speed > Vasya_speed:
        print("          Толя          ")
        print("  Петя                  ")
        print("                  Вася  ")
        print("   II      I      III   ")
    else:
        print("          Толя          ")
        print("  Вася                  ")
        print("                  Петя  ")
        print("   II      I      III   ")


#Q
a = float(input())
b = float(input())
c = float(input())

if a == 0 and b == 0 and c == 0:
    print('Infinite solutions')
elif a == 0 and b == 0:
    print('No solution')
else:

    if a == 0:
        x = -c / b
        print("{:.2f}".format(round(x, 2)))

    if b == 0 and c == 0:
        print("{:.2f}".format(round(0, 2)))

    if a != 0 and b == 0 and c != 0:  
        if ((- c) / a) < 0:
            print('No solution')  
        elif ((-c) / a) > 0:
            agg = abs(c / a) ** 0.5
            ag = agg
            ag2 = -agg
            afk = min(ag, ag2)
            afk2 = max(ag, ag2)
            print(round(afk, 2), round(afk2, 2))

    if a != 0 and b != 0 and c == 0:
        print("{:.2f}".format(0), "{:.2f}".format(round((-b / a), 2)))

    if a > 1:
        b = b / a
        c = c / a
        a = a / a

    if a != 0 and b != 0 and c != 0:
        d = ((b ** 2) - (4 * a * c))
        if d < 0:
            print('No solution')
        elif d == 0:
            ans1 = -b / 2 * a
            print("{:.2f}".format(round(ans1, 2)))
        else:
            x1 = (-b + d ** 0.5) / (2 * a)
            x2 = (-b - d ** 0.5) / (2 * a)
            prt1 = min(x1, x2)
            prt2 = max(x1, x2)

            if prt1 != prt2:
                print("{:.2f}".format(round(prt1, 2)), "{:.2f}".format(round(prt2, 2)))
            else:
                print("{:.2f}".format(round(prt1, 2))),


#R
a = int(input())
b = int(input())
c = int(input())
if (a * a + b * b == c * c) or (a * a + c * c == b * b) or (c * c + b * b == a * a):
    print("100%")
elif (a * a + b * b < c * c) or (a * a + c * c < b * b) or (c * c + b * b < a * a):
    print("велика")
else:
    print("крайне мала")




#S
x = float(input())
y = float(input())
r1 = 5
r2 = 10
c1 = (x ** 2 + y ** 2) ** 0.5 
c2 = (x ** 2 + y ** 2) ** 0.5  
y_para = (0.25 * (x ** 2)) + (0.5 * x) + 8.75

 
if x > 0 and y > 0:  
    if c1 <= r1: 
        print("Опасность! Покиньте зону как можно скорее!")
    elif c2 > r2:  
        print("Вы вышли в море и рискуете быть съеденным акулой!")
    else:  
        print("Зона безопасна. Продолжайте работу.")
elif x < 0 and y > 0: 
    if y <= 5 and y <= ((5 * x) + 35) / 3:
        print("Опасность! Покиньте зону как можно скорее!")
    elif c2 > r2: 
        print("Вы вышли в море и рискуете быть съеденным акулой!")
    else:
        print("Зона безопасна. Продолжайте работу.")
elif (x > 0 and y < 0) or (x < 0 and y < 0):  
    if y < y_para:  
        print("Опасность! Покиньте зону как можно скорее!")
    elif c2 > r2: 
        print("Вы вышли в море и рискуете быть съеденным акулой!")
    else:
        print("Зона безопасна. Продолжайте работу.")


#T
str_1 = input()
str_2 = input()
str_3 = input()

key_value = "зайка"

if key_value in str_1:
    if key_value in str_2:
        if key_value in str_2 and key_value in str_3:
            if str_1 < str_2 and str_1 < str_3:
                print(str_1, len(str_1))
            elif str_2 < str_1 and str_2 < str_3:
                print(str_2, len(str_2))
            elif str_3 < str_1 and str_3 < str_2:
                print(str_3, len(str_3))
        else:
            if str_1 < str_2:
                print(str_1, len(str_1))
            else:
                print(str_2, len(str_2))
    elif key_value in str_3:
        if str_1 < str_3:
            print(str_1, len(str_1))
        else:
            print(str_3, len(str_3))
    else:
        print(str_1, len(str_1))

elif key_value in str_2:
    if key_value in str_3:
        if str_2 < str_3:
            print(str_2, len(str_2))
        else:
            print(str_3, len(str_3))
    else:
        print(str_2, len(str_2))

else:
    print(str_3, len(str_3))