n=int(input('enter the limit'))
for i in range(n,0,-1):
  for j in range(n,i-1,-1):
     print(j,end="  ")
  print( )
for i in range(1,n+1):
  for j in range(n,i,-1):
     print(j,end="  ")
  print( )
