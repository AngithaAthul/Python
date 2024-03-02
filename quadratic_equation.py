a=int(input('enter a number'))
b=int(input('enter a number'))
c=int(input('enter a number'))
cal=b*b-4*a*c
if cal==0:
    cal=-b/2*a
    print(cal)
else:
    cal1=-b-cal/2*a
    cal2=-b+cal/2*a
    print(cal1,cal2)
    
