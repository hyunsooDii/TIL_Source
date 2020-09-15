# 자원의 정리

# finally - 예외 발생 여부와 상관없이 항상 호출, 작업의 마무리 작업(cleanup) 수행

import random

# def main():
#     try:
#         print("네트워크 접속")
#         a = 2/0
#         print("네트워크 통신 수행")
#     finally:
#         print("접속 해제")
#
#     print("작업 완료")
#
# main()

# def comm():
#     try:
#         print("네트워크 접속")
#         d = 0
#         if d != 0:
#             return
#         a = 2/d
#         print("네트워크 통신 수행")
#     except:
#         pass
#     finally:
#         print("접속 해제")
#
#     print("작업 완료")
#
# def main():
#     comm()
#
# main()

# assert - 단정한다

# def main():
#     score = 123
#     assert score <= 100, "점수는 100이하여야 합니다." # 단위 테스트할 때 사용
#     print(score)
#
# main()

# def main():
#     card = []
#     for _ in range(100):
#         if (card.count(random.randint(1, 48)) == 4):
#             break
#             card.insert(_, random.randint(1,48))
#         else:
#             card.insert(_, random.randint(1, 48))
#
#     print(card.count(30))
#     print(card)
#
#     player = int(input("게임 인원수 : "))
#     for _ in range(7):
#         for user_card in player:
#             card_ = card.pop()
#             user_card
#
#     print(arr)
#
# main()

def init(user_num):
    deck = list(range(1,49))
    random.shuffle(deck)

    users = [[] for _ in range(user_num)]
    return deck, users

def assign(deck, users):
    for _ in range(7):
        for user_card in users:
            card = deck.pop()
            user_card.append(card)

def print_result(deck, users):
    for n in range(len)