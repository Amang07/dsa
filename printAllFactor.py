# Extreme Brute force 
# n = int(input())
# for i in range(1,n+1):
#     if n % i== 0:
#         print(i)

# -------------------------------------------method 2------------------------------------------------------
# n = int(input())
# result=[]
# for i in range(1,(n//2)+1):
#     if n % i == 0:
#         result.append(i)        
# result.append(n)
# print(result)        

# -------------------------------------------method 2------------------------------------------------------
from math import *
n = int(input())
result=[]
for i in range(1,int(sqrt(n))+1):
    if n%i==0:
        result.append(i)
        if n//i != i:
            result.append(n//i)
result.sort()            
print(result)