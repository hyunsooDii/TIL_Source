import random

#
# student = 1
# while student <= 5 :
#     print(student, "번 학생의 성적을 처리합니다.")
#     student += 3
#

# num=1
#
# odd_total = 0
# even_total = 0
#
# while num <= 100 :
#     if num%2 == 0 :
#         even_total += num
#     else :
#         odd_total += num
#     num +=1
#
# print(odd_total)
# print(even_total)

# for student in [134,2,3,4,5]:
#     print(student, "번 학생의 성적을 처리한다")

# total = 0
# for num in range(1, 101) : # 범위의 끝 값은 포함하지 않는다. 즉 1<101 이란 뜻
#                             # for문의 초기값 0, 증가값 1 기본설정
#     total += num
#
# print("total =", total)
#
# total = 0
# for num in range(2, 101, 2) :
#     total += num
#
# print("total =", total)
#
# for a in range(5) :
#     print("이 문장을 반복합니다")

# cnt = 0
# for x in range(1, 51):
#     cnt += 1
#     if(x % 10) == 0:
#         print("+", end = '')
#     else:
#         print("-", end = '')
#
# print(cnt)

# ROCK = 1
# SCISSORS = 2
# PAPER = 3
#
# com_win = 0
# me_win = 0
# for loop in range(3):
#     com = (int(random.random()*10) % 3) + 1
#     print(loop+1,"번째 : ", end="")
#     me = int(input("바위 1, 가위 2, 보자기 3\n입력하시오 : "))
#
#     # 컴퓨터와 자신의 값 확인
#     if com == 1 :
#         print("com = Rock")
#     elif com == 2 :
#         print("com = Scissors")
#     elif com ==3 :
#         print("com = Paper")
#
#     if me == 1 :
#         print("me = Rock")
#     elif me == 2 :
#         print("me = Scissors")
#     elif me ==3 :
#         print("me = Paper")
#
#     # 가위바위보 승자 판단
#     if (com == me):
#         print("result = draw")
#     elif ((com == ROCK and me == SCISSORS) or (com == SCISSORS and me == PAPER) or (com == PAPER and me == ROCK)):
#         print("result = com win")
#         com_win += 1
#     else:
#         print("result = you win")
#         me_win += 1
#
#     loop += 1
#
# print("최종 결과 com = ", com_win, "번 승리, you = ", me_win, "번 승리")

# score = [92, 86, 68, 120, 56]
# for s in score :
#     if (s < 0) or (s > 100) :
#         print(s,"은 범위를 벗어났습니다.")
#         break
#     print(s)
#
# print("성적 처리 끝")
#
# for n in range(2,10):
#     print(n,"단")
#     for m in range(1,10):
#         print(n,"x",m,"=",n*m)
#     print()

# for n in range(1,10):
#     for m in range(n):
#         print("*",end="")
#     print()

# for y in range(1, 10):
#     print("*"*y)

# cnt = 0
# print("3 + 4 = ?")
# while True:
#     a = int(input("정답을 입력하세요: "))
#     cnt += 1
#     if cnt == 3:
#         print("기회3번 날렸습니다")
#         break
#     if a == 7:
#         print("참 잘했어요")
#         break


# print("3+4=?")
# for num in range(3):
#     a = int(input("정답을 입력하세요: "))
#     result = False
#     if a == 7:
#         result = True
#         break
# if result == True: print("참 잘했어요")
# else: print("실패했습니다")

for y in range(10,0,-1):
    print("*"*y)

