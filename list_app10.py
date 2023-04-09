
# HW-3: Fedor_xp28@student.itstep.org

try:
    word_list = []
    words = []
    for i in range(5):
        words.append(input("Enter word: "))
        sorted_words = sorted(words, key=lambda x: len(x))
    print(sorted_words)

except Exception as e:
    print(e)