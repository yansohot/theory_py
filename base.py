N = int(input())
print("Купи слона!\n" * N)

N = int(input())
M = int(input())
pieces = int(N * M // 2)
print(pieces)

num = int(input())
first = str(num // 1000)
second = str(num // 100 % 10)
third = str(num // 10 % 10)
fourth = str(num % 10)
new = second + first + fourth + third
print(new)

print('Как Вас зовут?')
name = input()
print(f'Здравствуйте, {name}!')
print('Как дела?')
mood = input()
if mood == "хорошо":
    print('Я за Вас рада!')
elif mood == "плохо":
    print('Всё наладится!')

pit = int(input())
vas = int(input())
tol = int(input())
if pit > vas:
    if pit < tol:
        print('1. Толя')
        print('2. Петя')
        print('3. Вася')
    elif pit > tol and vas > tol:
        print('1. Петя')
        print('2. Вася')
        print('3. Толя')
    elif pit > tol and vas < tol:
        print('1. Петя')
        print('2. Толя')
        print('3. Вася')
elif vas > pit:
    if vas < tol:
        print('1. Толя')
        print('2. Вася')
        print('3. Петя')
    elif vas > tol and tol > pit:
        print('1. Вася')
        print('2. Толя')
        print('3. Петя')
    elif vas > tol and tol < pit:
        print('1. Вася')
        print('2. Петя')
        print('3. Толя')

num = int(input())
first = num // 1000
second = num // 100 % 10
third = num // 10 % 10
fourth = num % 10
if first == fourth and second == third:
    print("YES")
else:
    print("NO")

num = int(input())
f = num // 100
s = num // 10 % 10
t = num % 10
n1 = s + t
n2 = f + s
if n1 > n2:
    conc = str(n1) + str(n2)
else:
    conc = str(n2) + str(n1)
print(conc)

count = 0
while (item := input()) != "Приехали!":
    if "зайка" in item:
        count = count + 1
print(count) 

a = int(input())
b = int(input())
while a != 0 and b != 0:
    if a > b:
        a = a % b
    else:
        b = b % a
print(a + b)

a = int(input())
fuck = 1
if a == 0:
    print(1)
else:
    for i in range(1, a + 1):
        fuck *= i
    print(fuck)