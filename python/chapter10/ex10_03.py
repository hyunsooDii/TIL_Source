# 집합 -  값의 중복을 허용하지 않음, 출력시 index 값은 정렬되지 않고 랜덤 출력

# def main():
#     print(set('aaabbbccc'))
#     print(set([12, 45, 56]))
#     print(set(('홍길동', '고길동', '둘리')))
#     print(set({'boy': '소년', 'school': '학교', 'book': '책'})) # 사전 즉, {} 은 공백이 될 수 없음, 사전의 키 목록을 집합으로 변환
#     print(set())
#
#     asia = {'korea', 'china', 'japan'}
#     asia.add('vietnam')
#     asia.add('korea')
#     asia.remove('japan')
#     print(asia)
#
# main()

def main():

    twox = {2, 4, 6, 8, 10, 12}
    threex = {3, 6, 9, 12, 15}

    print("교집합", twox & threex)
    print("합집합", twox | threex)
    print("차집합", twox - threex)
    print("배타적 차집합", twox ^ threex)

main()