# 지역 변수 - 함수 내에서 사용된 변수, 함수 내에서만 사용 가능

# def kim():
#     temp = "김과장의 함수"
#     print(temp)
#
# def lee():
#     temp = 2**10
#     return temp
#
# def park(a):
#     temp = a*2
#     print(temp)
#
# kim()
# print(lee())
# park(6)

# 전역 변수 - 어디서든 접근 가능한 변수, 탑 레벨에서 사용된 변수

# salerate = 0.9
#
# def kim():
#     print("오늘의 할인율 : ", salerate)
#
# def lee():
#     price = 1000
#     print("가격 : ", price * salerate)
#
# kim()
# salerate = 1.1
# lee()

# price = 1000
#
# def sale():
#     price = 500
#     print("sale", id(price))
#
# sale()
# print("global", id(price))

# 가급적 지역변수만 사용하라, 전역변수는 프로그램을 오동작시키는 근원이 된다
# price = 1000
#
# def sale():
#     global price # 전역 변수 선언
#     price = 500
#
# sale()
# print(price)

# 변수의 범위 - docstring, 함수의 도움말, help(함수명) 호출 시 출력될 문자열

# def calcsum(n):
#     """1~n 까지의 합계를 구해 리턴한다"""
#     total = 0
#     for i in range(n+1):
#         total += i
#
#     return total
#
# help(calcsum)

# def findMax(*ints):
#     max = ints[0]
#     for num in ints:
#       if(max < num):
#         max = num
#
#     return max
#
# num = findMax(4,5,1,3,2,-1,-7)
# print("max = ", num)

# def swap(x, y):
#     temp = y
#     y = x
#     x = temp
#
#     print("x", x)
#     print('y', y)
#
# a = 10
# b = 20
# swap(a, b)
#
# print('a', a)
# print("b", b)

# 함수는 스택이다
# Call by value - 복사본을 호출 한다
# 어떤 함수를 호출하든 스택 프레임이 생긴다

import random


# def rand(start, end):
#     """랜덤값 반환해주는 함수"""
#     return int(random.random()*(end-start)) + start
#     # return number
#
#
# def main(): # entry point
#     start = 1
#     end = 6
#     for n in range(5):
#         number = rand(start, end+1)
#         print(number)
#
#     help(rand)
#
# main()

import random

def rand(start, end):

    """랜덤값을 반환해주는 함수(시작 값, 끝 값)"""

    return int(random.random()*(end)) + start

def main():

    num = rand(1,100)
    cnt = 0
    print("com = ",num)

    for n in range(5):
        me = int(input(str(n+1)+ "번째 추측값 : "))
        
        if num < me:
            print(me,"보다는 작습니다.\n")
        elif num > me:
            print(me,"보다는 큽니다.\n")
        elif num == me:
            print("정답입니다")
            break

        cnt += 1

        if cnt == 5:
            print("실패했습니다. 정답은 ", num)
            break
main()