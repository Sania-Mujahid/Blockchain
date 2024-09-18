num1=int(input("enter 1st number "))
num2=int(input("enter 2nd number"))
num3=int(input("enter 3rd number"))
small=0
large=0
if num1<num2<num3|num1<num3<num2:
 print("small =",num1)
if num2<num1<num3|num2<num3<num1:
 print("small =",num2)
if num3<num1<num2|num3<num2<num1:
 print("small =",num3)
if num1>num2>num3|num1>num3>num2:
 print("large =",num1)
if num2>num1>num3|num2>num3>num1:
 print("large =",num2)
if num3>num1>num2|num3>num2>num1:
 print("large =",num3)
 print("smallest is",small)
 print("largest is",large)