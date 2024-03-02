#amstrong number using function
def amstrong(n):
    sum=0
    temp=n
    l=len(str(n))
   while temp>0:
        digit=temp%10
        sum+=digit**l
        temp//=10
    if n==sum:
        print("amstrong")
    else:
        print("not")
        
n=int(input("enter the number"))
amstrong(n)
