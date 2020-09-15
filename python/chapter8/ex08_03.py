# 포맷팅 (제일 사용빈도가 높음)

# def main():
#     month = 8
#     day = 15
#     anni = "광복절"
#     print("%d월 %d일은 %s이다." % (month, day, anni))
#
#     value = 123
#     print("###%d###" % value)
#     print("###%5d###" % value)
#     print("###%10d###" % value)
#     print("###%-10d###" % value)
#     print("###%1d###" % value)
#
# main()

# def main():
#     price = [30, 13500, 2000]
#     for p in price:
#         print("가격 : %d원" %p)
#     print()
#     for p in price:
#         print("가격 : %7d원" %p)
#     print()
#     for p in price:
#         print("가격 : %-7d원" %p)
#
# main()

# def main():
#     f = 123.1234567
#     print("%10f"%f)
#     print("%10.8f"%f)
#     print("%10.5f"%f)
#     print("%10f.2"%f)
#     print("%.2f"%f) # 제일 많이 씀
#
# main()

# def main():
#     # name = input("이름 : ")
#     # age = int(input("나이 : "))
#     # height = float(input("키 : "))
#     # print("이름 :{}, 나이:{}, 키:{:.2f}".format(name, age, height))
#
#     # name = input("이름 : ")
#     # age = int(input("나이 : "))
#     # height = float(input("키 : "))
#     print("이름 :{name}, 나이:{age}, 키:{height}".format(name="ㅇㅇ", age=15, height=140))
#
# main()

def main():
    name = "한결"
    age = 16
    height = 162.5
    print(f"이름:{name}, 나이:{age}, 키:{height:.2f}") # print문 뒤에 f를 붙임, 파이썬 3.6버전 이상 지원

main()

# 문자열은 불변 객체가, Slicing[:], Split, 포맷팅(3.6버전에서 쓸 수 있는 형식 추천) <- 문자열에서 중요한 키워드