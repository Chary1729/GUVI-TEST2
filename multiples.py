bell=[]
n=int(input())
for i in range(1,6):
  x=n*i
  bell.append(x)
  k=len(bell)
for j in range(k-1):
  print(bell[j],end=" ")
print(bell[k-1])
  
  
