from math import ceil, floor

word = input("Enter val = ")
length = len(word)
rem = int(not length % 2)
n_rem = length % 2


if n_rem:
    for row in range(length + rem):
        for col in range(length+1 +n_rem):
            if row + col == length//2 or row - col == length//2 or col - row == length//2+1+n_rem or row + col == length*2-length//2:
                print("*", end='\t')
            elif row == 0 and col == length//2+1:
                print("*", end='\t')
            elif row == length-1 and col == length//2+1:
                print("*", end='\t')
            elif row == length//2 and length >= col > 0:
                print(word[col - 1], end='\t')
            else:
                print(".", end='\t')
        print("")
else:
    for row in range(length + rem):
        for col in range(length+2):
            if row + col == length//2 or row - col == length//2 or col - row == length//2+1 or row + col == length*2-length//2+1:
                print("*", end='\t')
            elif row == length//2 and length >= col > 0:
                print(word[col - 1], end='\t')
            else:
                print(".", end='\t')
        print("")
