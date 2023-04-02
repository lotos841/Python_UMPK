
#A 
num = int(input())

for i in range(1, num + 1):
    for j in range(1, num + 1):
        print(i * j, end=" ")
    print()


#B
num = int(input())

for i in range(1, num + 1):
    for j in range(1, num + 1):
        print(f"{j} * {i} = {i * j}")


#C
num = int(input())
index = 1

row = 1
while index <= num:
    for col in range(row):
        print(f"{index}", end=' ')
        index += 1
        if index > num:
            break
    row += 1
    print()


#D
num_count = int(input())

sum = 0

for i in range(num_count):
    num = int(input())

    for j in range(int(len(str(num)))):
        sum += int(str(num)[j])
print(sum)


#E пока не работает
num = int(input())
key_word = "зайка"
count = 0

for i in range(num):
    while (phrase := input()) != "ВСЁ":
        if key_word in phrase:
            count += 1
print(count)