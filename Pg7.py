s = input("Enter string = ")
n = len(s)
rows =  n if n%2==1 else n+1
mid = n//2  + 1
for i in range(1,rows+1):
    for j in range(1,n+3):
        if(i==mid and j>1 and j<n+2):
            print(" {} ".format(s[j-2]),end="")
        elif(i+j == mid+1 or i-j==mid-1 or (j-i == mid+1 and n%2==1) or (j-i == mid and n%2==0) or i+j==(n+2+(mid))):
            print(" * ",end="")
        elif ((j>=mid and j<mid+3) and (i==1 or i==n) and n%2==1):
            print(" * ",end="")

        else:
            print(" - ",end="")
    print()
