n = int(input())
a = n
while(a>0):
    lastDigit = a % 10
    print(lastDigit)
    a = a //10
