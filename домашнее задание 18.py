def fact(n):
    if n == 0:
        return 1
    return fact(n-1) * n
x=int(input())
for i in range(x,0,-1):
    print(fact(i))

