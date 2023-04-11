# HW-3: Fedor_xp28@student.itstep.org

try:
    import random

    numbers = [random.randint(0, 100) for _ in range(10)]

    mean = sum(numbers) / len(numbers)

    count = sum(1 for num in numbers if num > mean)

    print("Numbers:", numbers)
    print("Mean:", mean)
    print("Number of items above mean:", count)

except :
    pass