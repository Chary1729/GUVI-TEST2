def sumOfAP(n,a,d) : 
    sum = 0
    i = 0
    while i < n : 
        sum = sum + a 
        a = a + d 
        i = i + 1
    return sum
n,a,d=input().split()
a=int(a)
d=int(d)
n=int(n)
print(sumOfAP(n,a,d))
  
