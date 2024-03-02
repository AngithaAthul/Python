#prime
srt=int(input('enter the starting point'))
stp=int(input('enter the ending point'))
for i in range(srt,stp+1):
  if srt==1:
    continue
  for j in range(2,i):
    if i%j==0:
      break
  else:
      print(i)
