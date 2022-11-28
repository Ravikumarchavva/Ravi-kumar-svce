x=[1,2,5,10,20,50,100,200,500,2000]
n=len(x)
x.sort(reverse=True)
i=int(input("enter a number"))
ans=0
for y in x:
    ans+=int(i/y)
    i-=int(i/y)*y
print(ans)