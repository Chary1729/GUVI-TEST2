N,k=input().split()
if(N.isdigit()==True and k.isdigit()==True):
  N=int(N)
  k=int(k)
  ans=1
for i in range(0,k):
    ans=ans*N
print(ans)
