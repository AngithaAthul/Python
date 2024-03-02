#armstrong number into a given range
srt=int(input('enter the starting point'))
stp=int(input('enter the ending point'))
for i in range(srt,stp+1):
  l=len(str(i))
  sum=0
  temp=i
  while temp>0:
    digit=temp%10
    sum+=digit**l
    temp//=10
  if i==sum:
    print(i)
