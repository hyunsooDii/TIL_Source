# 7단원 함수

# def int_sum(*numbers):
#     total = 0
#     for num in numbers:
#         total += num
#
#     return total
#
# print(int_sum(1,2,3))
# print(int_sum()) # 비어있는 매개변수, 실행됨

# 키워드 인수

# def calcstep(begin, end, step):
#     total = 0
#     for num in range(begin, end +1, step):
#         total += num
#
#     return total
#
# def main():
#     print("3 ~ 5 =", calcstep(3, 5, 1)) # 위치기반 호출 사용
#     print("3 ~ 5 =", calcstep(begin=3, end=5, step=1))  # 키워드 인수는 보통 4개이상의 인수를 받았을 때 사용
#     print("3 ~ 5 =", calcstep(step=1, end=5, begin=3))
#     print("3 ~ 5 =", calcstep(3, 5, step=1))
#     print("3 ~ 5 =", calcstep(3, step=1, end=5))
#
# main()

# 키워드 가변 인수 - 키워드 인수를 가변 개수로 전달할 때 사용하는 방법, **기호로 지정하여 타입은 사전이 됨

# def calstep(**args):
#     # begin = args['begin']
#     # end = args['end']
#     # step = args['step']
#     print(args)
#     print(type(args))
#     begin = args.get('begin')
#     end = args.get('end')
#     step = args.get('step',1) # 매개변수를 넘기지 않았을 경우, default 값을 정해줌 (dic함수에선 get메소드 권장)
#
#     total = 0
#     for num in range(begin, end +1, step):
#         total += num
#
#     return total
#
# def main():
#     print("3 ~ 5 = ", calstep(begin=3, end=5, step=1))
#     print("3 ~ 5 = ", calstep( end=5, begin=3))
#     dic = {'begin': 1, 'end': 5, 'step': 1}
#     calstep(begin=dic['begin'], end=dic['end'], step=dic['step'])
#     calstep(**dic) # 윗 줄과 동일
#
# main()

# 일반 변수, 가변 변수, 키워드 가변 변수 모두 사용

def calscore(name, *score, **option):
    print(name)
    total = 0
    for s in score:
        total += 5

    print("총점 : ", total)
    if(option.get('avg')):
        print("평균 : ", total/len(score))

def main():
    calscore("홍길동", 99, 88, 77, avg =True)
    calscore("고길동", 99, 88, 77, avg=False)

main()