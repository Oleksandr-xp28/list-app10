
# HW-3: Fedor_xp28@student.itstep.org

try:
    positive_numbers = []
    for num in range(0, 5):
        num = int(input("Enter a number: "))
        if num > 0:
            positive_numbers.append(num)
    print(positive_numbers)
except Exception as e:
    print("Error: ", e)
