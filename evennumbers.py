N,k=input().split()
if(N.isdigit()==True and k.isdigit()==True):
  N=int(N)
  k=int(k)
  count=0
  for i in range(N+1,k):
    if(i%2==0):
      count=count+1
      print(i)
