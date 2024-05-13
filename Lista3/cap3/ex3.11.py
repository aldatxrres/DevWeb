import math

for num in range(1, 101):
    if math.sqrt(num).is_integer():
        print(num)