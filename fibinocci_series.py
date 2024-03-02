#fibinocci series
l=int(input('enter the limit'))
f1=0
f2=1
if l<=0:
  print('no series')
elif l==1:
  print(f1)
elif l==2:
  print(f2)
else:
  print(f1)
  print(f2)
  l=l-2
  for i in range(l,0,-1):
    f3=f1+f2
    print(f3)
    f1=f2
    f2=f3
