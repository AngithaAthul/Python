#sum of fact
n=int(input('enter the number'))
sum=0
for i in range(1,n+1):
  if n%i==0:
    print(i)
    sum=sum+i
print('sum of factors of n ',sum)
