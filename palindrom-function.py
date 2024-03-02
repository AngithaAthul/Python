#palindrom or not
def palindrom(num):
   rev=0
  while num!=0:
     digit=temp%10
     rev=rev*10+digit
     temp//=10
  print(rev)
if num==rev:
  print("palindrom")
else:
  print("not")

num=int(input("enter the number"))
temp=num
palindrom(num)
