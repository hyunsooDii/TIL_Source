# 튜플 - 불변 자료 집합, 콤마가 중요
# 튜플은 여러개의 값을 리턴

import time

# def main():
#     score = 88, 95, 70, 100, 99
#     print(score)
#
#     score = 88,
#     print(score)
#
#     score = 88
#     print(score)
#
# main()

# def main():
#     a, b = 12, 45
#     print(a, b)
#
#     a, b = b, a
#     print(a, b)
#
# main()

# 튜플 활용 - 읽기만 가능한 목록을 만들 때, 복수개의 정보를 return하고 개별변수에 지정할 때

def gettime():
    now = time.localtime()
    return now.tm_hour, now.tm_min

def main():
    result = gettime()
    hour, minute = gettime()
    print(f"지금은 {hour}시 {minute}분 입니다.")

    score = [88, 95, 70, 100,99]
    tu = tuple(score) # 응용 : 읽기전용 파일을 수정하고 싶을 때, 변환함수를 이용하여 list로 만든 후 정보를 수정하고 tuple로 재변환
    print(tu)
    li = list(tu)
    li[0] = 100
    print(li)

main()