n=int(input('Enter a number'))
s=int(input('enter the first digit'))
while n!=0:
  d=n%10
  n//=10
if d==s:
  print('yes')
else:
  print('no')
