# 람다 함수

# filter - 시퀀스의 각 요소를 판정함수에 전달하여 True를 리턴하는 요소로만 구성된 새로운 시퀀스 리턴

# def flunk(s):
#     return s % 2 == 0
#
# def main():
#     score = [45, 89, 72, 53, 94]
#     for s in filter(flunk, score):
#         print(s)
#
#     even_list = list(filter(flunk, score)) # filter(True, False 리턴하는 매개변수, elements)
#     print(even_list)
#
# main()

# map - 시퀀스의 각 요소를 변환함수에 전달하고, 그 함수의 리턴값으로 구성된 새로운 시퀀스 리턴

# def half(s):
#     return s/2
#
# def total(s, b):
#     return s + b
#
# def main():
#     score = [45, 89, 72, 53, 94]
#     bonus = [2, 3, 0, 0, 5]
#     for s in map(half, score):
#         print(s, end=', ')
#     print()
#     for s in map(total, score, bonus):
#         print(s, end=', ')
# main()

# 람다 함수 - 한 줄로 정의되는 함수의 축약 표현

# def main():
#     score = [45, 89, 72, 53, 94]
#     for s in filter(lambda x: x<60, score):
#         print(s)
#
#     for s in map(lambda x: x/2, score):
#         print(s, end=', ')
#
# main()

def get_value(x): # x는 튜플로 가정
    return x[1]

def main():
    song = """by the rivers of babylon, there we sat down
    yeah we wept, when we remember zion.
    when the wicked carried us away in captivity
    required from us a song
    now how shall we sing the lord's song in a strange land"""

    alphabet = dict()
    for c in song:
        if c.isalpha() == False:
            continue

        c = c.lower()
        if c not in alphabet:
            alphabet[c] = 1
        else:
            alphabet[c] += 1

    alphabet_list = list(alphabet.items())
    alphabet_list.sort(key=lambda x : x[1])
    for a, c in alphabet_list:
        print(f"{a}:{c}")

main()
