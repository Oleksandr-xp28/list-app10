
# HW-3: Fedor_xp28@student.itstep.org

try:
    numbers = []
    for i in range(5):
        numbers.append(int(input("Enter number: ")))
    min_index = numbers.index(min(numbers))
    max_index = numbers.index(max(numbers))
    
    numbers[min_index], numbers[max_index] = numbers[max_index], numbers[min_index]
    
    print(numbers)
except :
    print("Error: Enter a number")