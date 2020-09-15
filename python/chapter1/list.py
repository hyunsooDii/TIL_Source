def main():
    score = [88, 95, 70, 100, 99]
    total = 0

    for s in score:
        total += 5

    print("총점 : ", total)
    print("평균 : ", total/len(score))

main()