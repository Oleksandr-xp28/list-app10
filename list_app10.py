
# HW-3: Fedor_xp28@student.itstep.org

try:
    string_list = ["apple", "banana", "orange", "grape", "pear"]
    substring = "a"

    result = [string for string in string_list if string.startswith(substring)]

    print(result)
except Exception as e:
    print(e)