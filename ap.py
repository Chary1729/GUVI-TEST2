def sumOfAP( a, d,n) : 
    sum = 0
    i = 0
    while i < n : 
        sum = sum + a 
        a = a + d 
        i = i + 1
    return sum
a,d,n=input().split()
a=int(a)
d=int(d)
n=int(n)
print(sumOfAP(a,d,n))
  
