# �������� 1: �������� ��������, ��� ������� ������ � n ���������� ����� 
# �� �������� ������� ������ �� �������� ����� � ������.
# HW-3: Fedor_xp28@student.itstep.org 

try:
    import random
    n = int(input('Enter n: '))
    lst = [random.randint(0, 100)]
    for i in range(n):
        if i % 2 == 0:
            print(i)
            print('Even:')
        else:
            continue
except Exception as e:
    print(e)
    print('Error')
finally:
    print('Good bye')
