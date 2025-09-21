n = int(input("Enter the number"))
b = n
a = n
count =0
ans = 0
while(a>0):
    ld = a % 10
    count+=1
    a = a // 10

while(n>0):
    ld = n % 10
    ans = (ld ** count) + ans
    n = n // 10    
if b == ans:
    print("armstrong")
else:
    print("not armstrong")