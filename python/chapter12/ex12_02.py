# 난수
# random 모듈

import random

# def main():
#     for i in range(5):
#         print("randint = ", random.randint(1, 10)) # 1부터 10사이 정수 (10 포함)
#     for i in range(5):
#         print("randrange = ", random.randrange(1, 10)) # 1부터 9사이 정수 (10 미포함)
#     for i in range(5):
#         print("uniform = ", random.uniform(1, 10)) # 1부터 9사이 실수 (10 미포함)
#
# main()

# def main():
#
#     print(random.choice(food)) # 시퀀스에서 랜덤하게 요소 선택하여 리턴
#
#     i = random.randrange(len(food))
#     print(food[i])
#
# main()

# def main():
#     food = ["짜장면", "짬뽕", "탕수육", "군만두"]
#     print(food)
#     random.shuffle(food) # 시퀀스의 내용을 랜덤하게 섞음, 셔플의 리턴값은 없음. 즉 food 리스트가 shuffle로 인해 값이 바뀜
#     print(food)
#
# main()

def main():
    nums = random.sample(range(1, 46), 6)
    nums.sort()
    print(nums)

main()