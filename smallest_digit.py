num=int(input("enter the number"))
s=9
for digit in str(num):
  digit=int(digit)
  if digit<s:
    s=digit
print('smallest',s)
