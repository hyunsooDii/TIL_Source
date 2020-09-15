# # 비밀번호를 만들어주는 함수 yoonHa()를 만들어봅시다.
# def yoonHa(nums):
#     dict_num = {4:"love", 8:"smile", 6:"kiss"}
#     for i in str(nums):
#         print(i)
#         tt = int(i)
#         #print(dict_num.get(tt), end="")
#
#
#
# # 채점을 위한 코드입니다. 이를 수정하지 마세요!
# nums = int(input())
# print(yoonHa(nums))

# def myMean(list):
#     mi = min(list)
#     ma = max(list)
#     list.remove(mi)
#     list.remove(ma)
#
#     avg = (sum(list) / len(list))
#
#     result = ','.join(map(str, list))
#
#     return f"{ma}(max), {mi}(min) 을 제외한 {result}의 평균 {avg}"
#
#
#
# ans = myMean([1, 2, 3, 4, 5])
# print(ans)

# answer = {"에릭":1, "김동완":2, "전진":3, "이민우":4, "앤디":5}
#
# def skyCastle(list):
#     list2=[]
#     for i in list:
#         list2.append( answer.get(i))
#
#     print(list2)
#
# skyCastle(["에릭", "이민우", "김동완", "전진"])

# def hot_cold(emotion):
#     cnt = 0
#     emotion[]

sang_geun = int(input())
sul = 0
while True:
    if (sang_geun % 5) == 0:
        sul = sul + (sang_geun//5)
        print(sul)
        break
    sang_geun = sang_geun-3
    sul += 1
    if sang_geun < 0:
        print("-1")
        break