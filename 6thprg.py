# 6) write a python p to take two user input and print their sum if the input are numeric and print the massage not posible if the inputs are string

num1 = input("enter numn1= ")
num2 = input("enter num2= ")

if num1.isdigit() and num2.isdigit() :
    num1=int(num1)
    num2=int(num2)
    print("sum=", num1+num2)
    
else:
  print("not possible", num1+num2)