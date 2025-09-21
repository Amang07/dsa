n = int(input())
a = n
ans = 0
while(a>0):
    ld = a % 10
    ans = (ans * 10) + ld 
    a = a //10
print(ans)    
