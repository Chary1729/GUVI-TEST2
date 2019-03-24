N,k=input().split()
if(N.isdigit()==True and k.isdigit()==True):
  N=int(N)
  k=int(k)
for val in range(N+1, k - 1): 
   if val > 1:
      for n in range(2, val):
        if (val % n) == 0:
          break
      else:
        print(val end=' ') 
