#Multiplication table
def mult(n):
    for i in range(1,10):
        print(i,"x",n,"=",i*n)
        
n=int(input("enter the number"))
mult(n)
