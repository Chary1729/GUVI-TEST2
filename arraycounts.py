my_honor=[]
N,K=int(input()), int(input())
x,y,z,a,b=int(input()),int(input()),int(input()),int(input()),int(input())
my_honor.append(x)
my_honor.append(y)
my_honor.append(z)
my_honor.append(a)
my_honor.append(b)
sum=0
for i in my_honor[0:K]:
  sum=sum+i
print(sum)
  
  
