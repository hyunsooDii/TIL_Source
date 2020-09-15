# 문자열 메소드
# .find(str): str 문자열을 찾아 인덱스 반환, 없으면 -1 반환
# .rfind(str) : 뒤에서 str 문자열을 찾아 인덱스 반환, 없으면 -1 반환
# .index(str) : find()와 동일, 없으면 예외 발생
# .count(str) : str 문자열이 몇번 등장하는지 리턴

# random.random = ramdom이라는 객체가 있고 random이라는 함수를 사용한다

# def main():
#     s = "Python programming"
#     print(len(s))
#     print(s.find('pro'))
#     print(s.rfind('po'))
#     print(s.index('Py'))
#     print(s.count('n'))
#
# main()

# .startwith, .endswitch 등은 메소드

# def main():
#     name = "홍길동"
#
#     if name.startswith("홍"):
#         print("홍씨 입니다.")
#
#     if name.startswith("김"):
#         print("김씨 입니다.")
#
#     file = "figure.jpg"
#
#     if file.endswith(".jpg"):
#         print("JPG그림 파일입니다.")
#
#     # s = "hello"
#     # s[2] = 'L' # 문자열은 불변객체 (부분 수정할 수 없다, 통째로 수정은 가능 )
#
# main()

# def main():
#     s = "Good morning. my love KIM"
#
#     print(s.lower())
#     print(s.upper())
#     print(s.swapcase())
#     print(s.capitalize())
#     print(s.title())
#     print(s)
#
#
# main() # split의 defalut값은 공백

# def main():
#     s = "짜장 짬뽕 탕수육"
#     print(s.split())
#
#     s2 = "서울->대전->대구->부산"
#     cities = s2.split("->")
#     print(cities)
#
#     for city in cities:
#         print(city)
#
# main()

# def main():
#     trabler = """
#     강나루 거너서
#     밀밭 길을
#
#     구름에 달 가듯이
#     가는 나그네
#     """
#
#     poet = trabler.splitlines()
#     for line in poet:
#         print(line)
#     print(len(poet))
#
# main()

# def main():
#     s = "._."
#     print(s.join("대한민국"))
#
#     print("._.".join("대한민국"))
#
# main()

def main():
    s = "독도는 일본땅, 대마도도 일본땅"
    print(s)
    print(s.replace("일본","한국"))
    print(s)

    message = "안녕하세요"

    print(message.center(30))
    print(message.ljust(30))
    print(message.rjust(30))

    trabler = """
    강나루 거너서
    밀밭 길을

    구름에 달 가듯이
    가는 나그네
    """

    poet = trabler.splitlines() # poet 는 list
    for line in poet:
        print(line.center(30))

main()