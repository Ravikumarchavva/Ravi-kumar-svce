def hanoi(n,start,end):
    if(n==1):
        print(start,end)
    else:
        other=6-(start+end)
        hanoi(n-1,start,other)
        print(start,end)
        hanoi(n-1,other,end)
n=int(input("enter number of discs :"))
hanoi(n,1,3)