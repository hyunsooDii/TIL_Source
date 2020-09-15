# 데코레이터

# 일급 시민 - 함수도 일반 변수와 동일한 특성을 가짐

# def add(a, b):
#     print(a+b)
#
# plus = add # 변수에 저장할 수 있다
# plus(1,2)

def calc(op, a, b): # 함수의 인자로 전달할 수 있다.
    op(a,b)

def add(a,b):
    print(a+b)

def multi(a, b):
    print(a * b)

calc(add, 1, 2)
calc(multi, 3, 5)