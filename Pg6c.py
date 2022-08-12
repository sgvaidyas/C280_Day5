def task1():
    s = str(input("Choose a word:\n"))
    sList = list(s)
    cnt = len(sList)

    pattern1 = "    " + (cnt - 2) * "* "
    pattern2 = "  " + "* " + (cnt - 2) * "  " + "*"

    print(pattern1)
    print(pattern2)
    print("* ", end="")
    for i in range(0, cnt):
        print(sList[i], end=" ")
    print("*")
    print(pattern2)
    print(pattern1)


def task2():
    s = str(input("Choose a word:\n"))
    sList = list(s)
    cnt = len(sList)

    pattern1 = "* * " + "      " + (cnt - 2) * "* " + "      " + "* *"
    pattern2 = "    " + "* " + "  " + "* " + (cnt - 2) * "  " + "* " + "  " + "* "

    print(pattern1)
    print(pattern2)
    print(3 * "  " + "* ", end="")
    for i in range(0, cnt):
        print(sList[i], end=" ")
    print("*")
    print(pattern2)
    print(pattern1)


def task3():
    s = str(input("Choose a word:\n"))
    sList = list(s)
    cnt = len(sList)
    if cnt % 2 == 0:
        pattern1 = (cnt//2) * "  " + 2 * "* "
        spaceCnt = 2
    else:
        pattern1 = (cnt//2) * "  " + 3 * "* "
        spaceCnt = 3
    print(pattern1)

    for i in range((cnt // 2) - 1, 0, -1):
        pattern2 = i * "  " + "* " +spaceCnt * "  " + "*"
        spaceCnt += 2
        print(pattern2)

    print("* ", end="")
    for i in range(0, cnt):
        print(sList[i], end=" ")
    print("*")

    spaceCnt -= 2
    for i in range(1,(cnt // 2)):
        pattern2 = i * "  " + "* " +spaceCnt * "  " + "*"
        spaceCnt -= 2
        print(pattern2)

    print(pattern1)


if __name__ == '__main__':
    task3()
