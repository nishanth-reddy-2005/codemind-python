def gcd(a,b):
    if(a%b==0):
        return b
    else:
        return gcd(b,a%b)
t=int(input())
for i in range(t):
    n,a,b,k=map(int,input().split())
    tot=(n//a)+(n//b)
    lcm=(a*b)//gcd(a,b)
    tot-=(2*(n//lcm))
    if(tot>=k):
        print("Win")
    else:
        print("Lose");