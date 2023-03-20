#sum of prime factor 
'''def isPrime(num):
    if(num==2):
        return True
    for i in range(2,num//2+1):
        if(num%i==0):
            return False
    return True    


def isPrimeLargest(num):
    for i in range(num,1,-1):
        if(num%i==0 and isPrime(i)):
           return i
        
n=int(input())
l=[]
for i in range(0,n):
    l.append(i+n)
l=[10,11,12,13,14,15,16,17,18]
l2=[]
for i in l:
    val = isPrimeLargest(i)
    l2.append(val)
print(l)    
print(l2)
print(sum(l2))
