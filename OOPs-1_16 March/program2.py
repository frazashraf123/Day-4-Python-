#Q1.nearest_palindrome
def isPalindrome(n):
    if(n<0):
        n=n*(-1)
    st = str(n)
    if(st==st[::-1]):
        return True
    else:
        return False
n=int(input())
i=n+1
while(True):    
    if(isPalindrome(i)):
       ans=i
       break
    i+=1
print(ans)

#or
import sys
def nextPal(num):
    for i in range(num+1,sys.maxsize):
        if(str(i)==str(i)[::-1]):
            return i
print(nextPal(99))        
