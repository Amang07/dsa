n = int(input("enter the number"))
a = n
ans = 0
while(a>0):
    ld = a % 10
    ans = (ans * 10) + ld
    a = a//10
if ans == n:
    print("number is palindrome")
else:
    print("number is not palindrome")        