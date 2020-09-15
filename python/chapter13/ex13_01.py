# 예외 처리

# def main():
#     str = input("점수를 입력하세요 : ")
#     try:
#         score = int(str)
#         print("입력한 점수 : ",score)
#     except:
#         print("예외가 발생하였습니다.")
#     else:
#         print("작업완료")
#
# main()

# 예외의 종류

# def main():
#     str = "89"
#     try:
#         score = int(str)
#         print(score)
#         a = str[5]
#     except ValueError:
#         print("점수의 형식이 잘못되었습니다.")
#     except IndexError:
#         print("첨자 범위를 벗어났습니다.")
#
#     print("작업 완료")
#
# main()

# def main():
#     str = "89"
#     try:
#         score = int(str)
#         print(score)
#         a = str[5]
#     except (ValueError, IndexError):
#         print("점수의 형식이나 첨자가 잘못되었습니다.")
#
#     print("작업 완료")
#
#
# main()

# def test(str):
#     score = int(str)
#     print(score)
#
#
# def word():
#     str = "89d"
#     # test(str)
#     try:
#         score = int(str)
#         print(score)
#     except ValueError as e:
#         e.print
#         print(e)
#     except IndexError as e:
#         print(e)
#
#     else:
#         print("작업 완료")
#
# def main():
#
#     word()
#
# main()

# def test(str):
#     score = int(str)
#     print(score)
#
# def word():
#     str = "89d"
#     try:
#         test(str)
#     except Exception as e: # 모든 경우의 예외
#         print(e)
#
#     else:
#         print("작업 완료")
#
# def main():
#
#     word()
#
# main()

def calcsum(n):
    if n < 0:
        raise ValueError # 개발자에 의해 임의로 예외를 발생시킴

    total = 0
    for i in range(n+1):
        total += i
    return total

def main():
    try:
        print("~10 = ", calcsum(10))
        print("~-5 = ", calcsum(-5))

    except Exception:
        print("오류")

    else:
        print("실행완료.")

main()