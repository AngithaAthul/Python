n=int(input('enter the limit'))
c=1
for i in range(n+1):
  for j in range(i):
     print(c,end="  ")
     c=c+1
  print(  )
