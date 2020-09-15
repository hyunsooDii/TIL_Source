# 제너레이터 - 객체로 순회가능한 객체를 만드는 거는 다소 귀찮은 작업, 제너레이터 함수로 대체 가능

def seqgen(data):
    for index in range(0, len(data), 2):
        yield data[index:index+2] # return과 다르게 yield는 함수가 끝나는 것이고 순회 가능 객체로 순회할 때 실제 함수가 실행

def main():

    solarterm = seqgen("입춘우수경칩춘분청명곡우입하소만망종하지소서대서")
    # 제너레이터함수를 호출하는 행위는 __init__과 __next__를 갖고 있는 객체로 변환한다는 뜻
    print(solarterm)

    for k in solarterm:
        print(k, end=',')

main()