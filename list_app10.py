# Завдання 2: Реалізуйте функцію, яка приймає список чисел та повертає список з унікальними елементами, 
# зберігаючи їх порядок.

# HW-3: Fedor_xp28@student.itstep.org
try:
    list = []
    u_list = []
    for x in range(0, 5):
        list.append(int(input('Enter list: ')))
        for item in list:
            if item not in u_list:
                u_list.append(item)
    print(u_list)
except Exception as e:
    print(e)
    print("Erorr")