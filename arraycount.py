N,K=int(input()), int(input())
print(N,K)
hello_array=[]
for i in range(1,N+1):
  hello_array.append(i)
print(hello_array)
sum=0
for i in hello_array[0:K]:
  sum=sum+i
print(sum)
  
  
