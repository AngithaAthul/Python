n=int(input('enter the limit'))
num=1
for i in range(n):
  for j in range(i,n):
     print(num,end="  ")
     num+=1
  num=1   
  print( )
for k in range(2,n+1):
  for m in range(1,k+1):
    print(m,end="  ")
  print( )
