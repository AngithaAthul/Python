#multiplication table into a given range
srt=int(input('enter the starting point'))
stp=int(input('enter the ending point'))
for i in range(srt,stp+1):
  print('multiplication table ',i)
  for j in range(1,10):
     print(j,'x',i,'=',i*j)
