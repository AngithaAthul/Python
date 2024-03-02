basic_sal=float(input('Enter the basic salary'))
if basic_sal>=50000:
     percent_allowance=float(input('Enter the percentage of allowance'))
     percent_deduction=float(input('Enter the percentage of deduction'))
     net_sal=basic_sal+(basic_sal*percent_allowance/100)-(basic_sal*percent_deduction/100)
     print('The net salary is:',net_sal)
else:
    print('salary is less than 50k')
