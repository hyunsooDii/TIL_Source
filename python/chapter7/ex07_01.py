# 함수는 코드중복을 방지하기 위해 만듬, 코드 재사용성
# 반복되는코드 = 함수로 정의하여 반복을 없앰

def calcsum(n):
    total = 0
    for num in range(n+1):
        total += num

    return total

print(" ~ 4 = ", calcsum(4))
print(" ~ 10 = ", calcsum(10))

