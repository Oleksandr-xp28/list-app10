
# HW-3: Fedor_xp28@student.itstep.org

try:
    import random
    list1 = [random.randint(1, 10) for i in range(10)]
    list2 = [random.randint(1, 10) for i in range(10)]

    print(list1)
    print(list2)
    common_elements = list(set(list1).intersection(set(list2)))

    print(common_elements)
except Exception as e:
    print(e)
finally:
    print("The End")