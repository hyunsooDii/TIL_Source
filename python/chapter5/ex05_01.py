import random
# x와 y의 값 교환
#
# x = 10
# y = 20
#
# print("기존 x 값 = ", x)
# print("기존 y 값 = ", y)
#
# z = x
# x = y
# y = z
#
# print("교환 한 x 값 = ", x)
# print("교환 한 y 값 = ", y)
#
# 가위 바위 보 게임, 1: rock, 2: scissors, 3: paper

ROCK = 1
SCISSORS = 2
PAPER = 3



com = (int(random.random()*10) % 3) + 1
print(com)
me = int(input("바위 1, 가위 2, 보자기 3\n입력하시오 : "))

# 컴퓨터와 자신의 값 확인
if com == 1 :
    print("com = Rock")
elif com == 2 :
    print("com = Scissors")
elif com ==3 :
    print("com = Paper")

if me == 1 :
    print("me = Rock")
elif me == 2 :
    print("me = Scissors")
elif me ==3 :
    print("me = Paper")

# 가위바위보 승자 판단
    if (com == me):
        print("result = draw")
    elif ((com == ROCK and me == SCISSORS) or (com == SCISSORS and me == PAPER) or (com == PAPER and me == ROCK)):
        print("result = com win")
    else:
        print("result = me win")

