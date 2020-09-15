# 함수 데코레이터

# 지역 함수 - 함수 안에 함수를 정의해서 사용

# def calcsum(n): # 지역함수
#     def add(a, b): # 이름 충돌을 막기 위해 지역함수 사용
#         return a + b
#
#     total = 0
#     for i in range(n+1):
#         total = add(total, i)
#
#     return total
#
# print("~ 10 = ", calcsum(10))

# def makeHello(message):
#     def hello(name):
#         print(message + ", " + name)
#     return hello
#
# enghello = makeHello("Good Morning") # closure 변수 -> makeHello함수 message 지역변수
# kohello = makeHello("안녕하세요") # closure 변수
#
# # 지역함수인 경우 함수를 호출했을 때 매개변수를 stack에 저장하는게 아니라 heap에 저장, 즉 함수 호출이 끝나도 매개변수는 유지
#
# enghello("Mr Kim") # makeHello 내부 hello함수 name 지역변수
# kohello("홍길동")

# 함수 데코레이터 - 함수를 래핑하여 함수의 앞 또는 뒤에 코드를 자동으로 추가

# def inner(): # 데코레이터 작업 전
#     print("결과를 출력합니다.")
#
# def outer(func): # 데코레이터 작업 전
#     print("-"*20)
#     func()
#     print("-"*20)
#
# outer(inner)
#
# def hello():
#     print("안녕하세요")
#
# outer(hello)

# def inner(): # 데코레이터 작업 후
#     print("결과를 출력합니다.")
#
# def outer(func): # 데코레이터 작업 전
#     def wrapper(): # 전처리
#         print("-"*20)
#         func()
#         print("-"*20)
#     return wrapper # 후처리
#
# inner = outer(inner)
# inner()

# def outer(func):
#     def wrapper():
#         print("-"*20)
#         func()
#         print("-"*20)
#     return wrapper
#
# @outer # inner = outer(inner)<- 이 문장을 실행했다고 가정
# def inner():
#     print("결과를 출력합니다.")
#
# inner()

# 클래스 데코레이터 - __callable__메소드

class Outer:
    def __init__(self, func):
        self.func = func

    def __call__(self): # 클래스를 함수 호출하듯이 사용했을 때 호출되는 메소드
        print("-"*20)
        self.func()
        print("-"*20)

def inner():
    print("결과를 출력합니다")

# inner = Outer(inner) # 클래스를 함수 호출하듯이 사용했을 때
# inner()

@Outer
def inner():
    print("결과를 출력합니다.") # + 데코레이터

inner()