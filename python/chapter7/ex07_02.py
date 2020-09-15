# 인수 = 함수로 값을 전달했을 때 이를 저장하는 변수

# def calcrange(begin, end):
#     total = 0
#     for num in range(begin, end+1):
#         total += num
#
#     return total
#
# print("3 ~ 7 = ", calcrange(3,7))

# def printsum(n):
#     total = 0
#     for num in range(n+1):
#         total += num
#     print("~", n, "=", total)
#
# printsum(4)
# printsum(10)
#
# a = printsum(4)
# print(a)

# def calctotal(): # 함수는 반드시 코드 블럭이 있어야 함, 실제 구현을 나중으로 미루고자 할 때 pass 지정
#     # 나중에 구현할 것
#     pass

# * <- 튜플 인자를 표기하는 기호

# def intsum(*ints):
#     total = 0
#     for num in ints:
#         total += num
#
#     return total
#
# print(intsum(1, 2, 3))
# print(intsum(5, 7, 9, 11, 13))
# print(intsum(8, 9, 6, 2, 9, 7, 5, 8))

# 인수의 기본 값 - 함수 호출시 인수가 지정되지 않았을 때 사용할 값, 중간에 배정시 구분 불가
def calcstep(begin, end, step = 1):
    total = 0
    for num in range(begin, end +1, step):
        total += num

    return total

print("1 ~ 10 = ", calcstep(1, 10, 2))
print("2 ~ 10 = ", calcstep(1, 100))

# 블랙박스 : 코드를 봤을 때, 어떤식으로 코딩했는지 알 수 없는 경우? 함수를 사용하는데 지장은 없음
# 화이트박스 : 코드를 봤을 때, 어떤식으로 코딩했는지 알 수 있는 경우?           "

