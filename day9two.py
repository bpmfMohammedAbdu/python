def calculater (num1,num2):
    num1=int(input("inter first number "))
    num2=int(input("inter seconde number"))
    #sum=num1+num2
    difference=num1-num2
    division =num1/num2
    product=num1*num2
    modulo=num1%num2
    power=num1**num2
    #print(f"the  difference of {num1}and{num2} is {num1-num2}")
    print(f"the  difference of {num1}and{num2} is {num1-num2}")
    print(f"the  divison of {num1}and{num2} is {num1/num2}")
    print(f"the  modulof {num1}and{num2} is {num1%num2}")
    print(f"the  power of {num1}and{num2} is {num1**num2}")
    return num1+num2
    return (f"the  difference of {num1}and{num2} is {num1-num2}")
print(calculater(4,4))
