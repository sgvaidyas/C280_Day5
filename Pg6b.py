def task4():
    s = str(input("Choose a word:\n"))
    sList = list(s)
    cnt = len(sList)

    # First and last line
    if cnt % 2 == 0:
        pattern1 = "* * " + (cnt-1) * "  " + 2 * "* " + (cnt-1) * "  " + "* * "
        spaceCnt = 2
    else:
        pattern1 = "* * " + (cnt-2) * "  " + 3 * "* " + (cnt-2) * "  " + "* * "
        spaceCnt = 3
    print(pattern1)

    # Second pattern
    spaceCnt2 = 2
    for i in range((cnt // 2) - 1, 0, -1):
        pattern2 = spaceCnt2 * "  " + "* " + (i*2-1) * "  " + "* " + spaceCnt * "  " + "* " + (i*2-1) * "  "  + "* "
        spaceCnt += 2
        spaceCnt2 += 1
        print(pattern2)

    # Middle line
    print(spaceCnt2*"  "+"* ", end="")
    for i in range(0, cnt):
        print(sList[i], end=" ")
    print("*")

    spaceCnt -= 2
    spaceCnt2 -= 1
    for i in range(1, (cnt // 2)):
        pattern2 = spaceCnt2 * "  " + "* " + (i*2-1) * "  " + "* " + spaceCnt * "  " + "* " + (i*2-1) * "  "  + "* "
        spaceCnt -= 2
        spaceCnt2 -= 1
        print(pattern2)

    print(pattern1)


if __name__ == '__main__':
    task4()
