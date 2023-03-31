# спать круче

#1 

for i in range(20,31,1):
    print(i)

#2 

for i in range(0,101,10):
    print(i)

#3

for i in range(10,26):
    print(i, i + 0.4)


#4

for i in range(1,21):
    print(i, round(i*20.40,2),"r")

#5 

N = int(input("введите число: "))

for i in range(1,11):
    print(N, " * ", i, " = ", N * i)

#6

number1 = int(input("Введите количество сов: "))
for i in range(1, number1+1):
    print(" :)\_____/(:" * i)
    print("  {(@)v(@)} " * i)
    print("  {|~- -~|} " * i)
    print("  {/^'^'^\} " * i)
    print("  ===m-m=== "* i)

#7

a = int(input())
b = int(input())

for i in range(a - (a + 1) % 2, b - b % 2, 2):
    print(i, end=' ')

#8

a = 10
b = 1

if a < b: 
    for i in range(a,b+1):
        print(i, end=" ")
else:
    for i in range(a,b-1, -1):
        print(i, end=" ")


#9

n = int(input("число: "))
for i in range(10**n - 1, 10**(n - 1) - 1, -2):
    print(i)

#10

for i in range(11, 99):
    a=i%10
    b=i//10
    if 2*(a+b)==a*b:
        print(i)


#11

a = 1000
b = 3000
for i in range(a // 100, 100):
    n = i * 100 + i % 10 * 10 + i // 10
    if n >= a:
        if n <= b:
            print(n)

