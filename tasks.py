limit = int(input())

counter = 0
width = 1
max_length = 0

while counter <= limit:
    string_length = 0
    for position in range(width):
        counter += 1
        if counter <= limit:
            string_length += len(str(counter))
        if position < width - 1 and counter < limit:
            string_length += 1

    if max_length < string_length:
        max_length = string_length

    width += 1

counter = 0
width = 1

while counter <= limit:
    string = ''
    for position in range(width):
        counter += 1
        if counter <= limit:
            string += str(counter)
        if position < width - 1 and counter < limit:
            string += ' '
    width += 1
    print(f'{string:^{max_length}}')


# Наивный метод

height = int(input())
width = int(input())

ceil_width = len(str(width * height))

for row in range(height):
    for column in range(width):
        if column % 2 == 0:
            num = column * height + row + 1
        else:
            num = (column + 1) * height - row
        print(f'{num:>{ceil_width}}', end=' ')
    print()


# Наивный метод

height = int(input())
width = int(input())

cell_width = len(str(height * width))

for i in range(1, height + 1):
    for j in range(width * (i - 1) + 1, width * i + 1):
        print(f'{j:>{cell_width}}', end=' ')
        if j == width * i:
            print()


num = int(input())

first = num // 100
second = num // 10 % 10
third = num % 10

if max(first, second, third) != first and min(first, second, third) != first:
    middle = first
elif max(first, second, third) != second and min(first, second, third) != second:
    middle = second
else:
    middle = third

if max(first, second, third) + min(first, second, third) == middle * 2:
    print('YES')
else:
    print('NO')