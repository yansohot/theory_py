from math import log, cos, sin, pi, e

x = float(input())

log32 = log(x ** (3 / 16)) / log(32)
cos_part = cos(pi * x / (2 * e))
sin_part = sin(x / pi)**2

result = log32 + x ** cos_part - sin_part

print(result)

import math
import sys

def compute_gcd(numbers):
    current_gcd = numbers[0]
    for num in numbers[1:]:
        current_gcd = math.gcd(current_gcd, num)
        if current_gcd == 1:
            break  # НОД не может быть меньше 1
    return current_gcd

# Чтение строк из стандартного ввода
for line in sys.stdin:
    numbers = list(map(int, line.strip().split()))
    if not numbers:
        continue  # Пропускаем пустые строки
    print(compute_gcd(numbers))