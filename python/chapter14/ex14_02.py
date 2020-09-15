# 파일 관리 함수 - shell utility

import shutil
import os

# def main():
#     shutil.copy("live.txt", "live2.txt")
#
# main()

# def main():
#     files = os.listdir('C:/')
#     for f in files:
#         print(f)
#
# main()

def dumpdir(path):
    files = os.listdir(path)
    for f in files:
        fullpath = os.path.join(path, f) # 디렉터리와 파일을 결합할 때 사용
        if os.path.isdir(fullpath):
            print(f"{fullpath}")
            dumpdir(fullpath) # 재귀 호출
        else:
            print("\t" + f)

def main():
    dumpdir("/workspace")

main()