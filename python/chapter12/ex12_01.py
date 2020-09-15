# 표준모듈
# 모듈 - 재사용 가능한 코드블럭
# 수학
# math 모듈 - pi(원주율 상수), tau(원주율의 2배되는 상수), e(자연 대수 상수), inf(무한대 값), nan(숫자가 아닌 값을 의미)
# 함수 - sqrt, pow, hypot, factorial, sin, cos, tan, degrees, radians, ceil, floor, fabs, trunc, log, log10, gcd

import math
import time
from datetime import datetime
import calendar as cal

# def main():
#     print(math.sqrt(3))
#
# main()

# 통계 모듈, statistics
# 시간조사, time 모듈

# def main():
#     print(time.time())
#
# main()

# def main():
#     t = time.time()
#     print(time.ctime(t)) # ctime (character time)
#
# main()

# def main():
#     t = time.time()
#     print(time.localtime(t))
#
# main()

# def main():
#     now = time.localtime()
#
#     print(f"{now.tm_year}년{now.tm_mon}월{now.tm_mday}일")
#     print(f"{now.tm_hour}:{now.tm_min}:{now.tm_sec}")
#
#     now = datetime.datetime.now() # 모듈명, 객체명, 메소드 순 , 위에 from datetime import datetime 모듈 선언하는게 좋음
#
#     print(f"{now.year}년{now.month}월{now.day}일")
#     print(f"{now.hour}:{now.minute}:{now.second}")
#
# main()

# def main():
#     start = time.time()
#     total = 0
#     for a in range(1000):
#         total += a
#         print(total)
#     end = time.time()
#
#     print(end - start)
#
# main()

# def main():
#     print("안녕하세요")
#     time.sleep(1) # sleep 은 초단위
#
#     print("밤에 성시경이 두 명 있으면 뭘까요?")
#     time.sleep(5)
#     print("야간투시경 입니다.")
#
# main()

# def main():
#     print(cal.calendar(2015))
#     print(cal.month(2019, 1))
#
# main()

# def main():
#     dates = ['월', '화', '수', '목', '금', '토', '일']
#
#     day = cal.weekday(2020, 8, 15)
#     print(f"광복절은 {dates[day]}요일입니다.")
#
# main()

# def main():
#     print(time.strftime('%Y-%m-%d %I:%M'))
#     timestring = '2019-02-20 12:12:12'
#     print(time.strptime(timestring, '%Y-%m-%d %I:%M:%S'))
# main()

# def main():
#     print(time.strftime("%Y-%m-%d %I:%M:%S"))
#
#     now = datetime.now()
#     print(now.strftime("%Y-%m-%d %H:%M:%S.%f")) # 초 소수점 6번째 까지 출력
#
# main()

def main():
    now = datetime.now()
    for _ in range(10):
        fname = now.strftime(f"%Y%m%d%I%M%S-{_+1:03d}.jpg") # f열은 문자열이면 다 가능
        print(fname)

main()