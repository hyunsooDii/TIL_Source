# 리스트 관리
# 데이터를 조작하는 행위 CRUD (Create, Read, Update, Delete)

# .append(값) - 리스트의 끝에 값을 추가
# .insert(위치, 값) - 지정한 위치에 값을 삽입

import random
import re

# def get_randomList(range_count, start, end):
#     ran_nums = []
#
#     for _ in range(range_count): # 관례상 의미없는 변수는 ' _ ' 사용
#         num = random.randint(start, end)
#         ran_nums.append(num)
#
#     return ran_nums
#
# def main():
#
#     ran_nums = []
#
#     print(get_randomList(10, 1, 10))
#
# main()

# def main():
#     nums = [1, 2, 3, 4]
#     nums[2:2] = [90, 91, 92] # 3번째 index에 삽입
#     print(nums)
#
#     nums = [1, 2, 3, 4]
#     nums[2] = [90, 91, 92] # 지정한 위치의 엘리먼트에 리스트 대체, 리스트값은 한개
#     print(nums)
#
# main()

# def main():
#     list1 = [1, 2, 3, 4, 5]
#     list2 = [10, 11]
#     list3 = list1 + list2
#     print(list3)
#     list1.extend(list2)
#     print(list1)
#
# main()

# def main():
#     score = [88, 95, 70, 100, 99, 88, 78, 50]
#     score.remove(100)
#     print(score)
#
#     del (score[2])
#     print(score)
#
#     score[1:4] = []
#     print(score)
#
# main()

# def main():
#     score = [88, 95, 70 , 100, 99]
#     print(score.pop())
#     print(score)
#     print(score.pop())
#     print(score)
#     print(score.pop(1))
#     print(score)
#
# main()

# def main():
#
#     score = [88, 95, 70, 100, 99]
#     score.append(50)
#     print("큐 ", score)
#     print("큐 ", score.pop(0))
#     print("큐 ", score)
#
#     score2 = [88, 95, 70, 100, 99]
#     score2.append(50)
#     print("스택 ", score2)
#     print("스택 ", score2.pop())
#     print("스택 ", score2)
#
# main()

# def main():
#     ans = input("결제 하시겠습니까? ")
#
#     if ans in ['yes', 'y', 'ok', '예']:
#         print("결제를 진행합니다")
#     else:
#         print("결제를 취소합니다")
#
# main()

# def main():
#
#     score = [88, 95, 70, 100, 99]
#     score.sort()
#     print(score)
#     score.reverse()
#     print(score)
#
#     score2 = [5, 14, 36, 56, 21]
#     score2.sort(reverse=True)
#     print(score2)
#
#     country = ["Korea", "Japan", "CHINA", "america"]
#     # country.sort()
#     # print(country)
#     # country.sort(key = str.lower) # key 오른쪽에는 함수를 주면 된다. 오른쪽 함수로 변환시켜 정렬 시킨다.
#     # print(country)
#
#     for _ in range(len(country)):
#         country[_] = country[_].lower()
#     print(country)
#
#     sorted_country = sorted(country)
#     print(sorted_country)
#
#     score = [88, 95, 70, 100, 99]
#     sorted_score = sorted(score) # sorted - 원본은 유지하면서 정렬을 하고 싶은 경우 사용
#     print(score)
#     print(sorted_score)
#
# main()


# def main(): # 컴프리핸션은 비어있는 리스트에 반복적으로 값을 채우는 것에 사용
#     country = ["Korea", "Japan", "CHINA", "america"]
#
#     newlist = [c.lower() for c in country if c == "Korea"]
#     print(newlist)
#
#     print([n/2 for n in range(1,11) if n % 3 == 0])
#
#     random_num = [random.randint(1, 100) for _ in range(10)]
#     print(random_num)
#
# main()

# slicing , append, pop, sort, 컴프리핸션 중요

# HANGMAN = """
# ---+
#    ㅣ
#    o
#   /ㅣ\\
#    / \\
# """
#
# def main():
#
#     hang = HANGMAN.splitlines()
#     com = random.randint(1, 100)
#
#     print(com)
#
#     for i in range(5):
#         me = int(input(str(i+1) + "번째 추측 값 : "))
#         if(me > com):
#             print(f"{me}보다 작습니다.")
#         elif(me < com):
#             print(f"{me}보다 큽니다.")
#         elif(me == com):
#             print("정답입니다.")
#             break;
#         print(*hang[1:i+2],sep="\n")
# main()

HANGMAN = """
  ㅣ
   o
  /ㅣ\\
   / \\
"""

def main():

    hang = HANGMAN
    hang2 = hang.replace(" ","")
    hang3 = [x for x in hang2 if x]
    hang3.remove('\n')
    hang4 = [x for x in hang3 if x]
    hang4.remove('\n')
    hang5 = [x for x in hang4 if x]
    hang5.remove('\n')
    hang6 = [x for x in hang5 if x]
    hang6.remove('\n')
    hang7 = [x for x in hang6 if x]
    hang7.remove('\n')
    print(hang7)




    com = random.randint(1, 100)
    print(com)


    for i in range(5):
        me = int(input(str(i+1) + "번째 추측 값 : "))
        if(me > com):
            print(f"{me}보다 작습니다.")
        elif(me < com):
            print(f"{me}보다 큽니다.")
        elif(me == com):
            print("정답입니다.")
            break;
        print(*hang7[0:i+1],sep="\n")
main()