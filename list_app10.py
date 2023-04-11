
# HW-3: Fedor_xp28@student.itstep.org
try:
    squared_numbers = []
    for num in range(0, 5):
        num = int(input("Enter a number: "))
        squared_numbers.append(num**2)
    print(squared_numbers)
except :
    print("Error: Enter a number")