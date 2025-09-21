# n = int(input())
# a = n
# count = 0
# while(a > 0):
#     ld = a % 10
#     count+=1
#     a = a //10
# print(count)    #here the time complexity is O(logbase10(a))


# ------------------method2---------------------------------
from math import *
n = int(input())
print(int(log10(n))+1)