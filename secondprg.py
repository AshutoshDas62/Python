# wap to find if user input number is divisible by 2,3,5 or all.
num= int(input("enter a nmber"))
if(num%2==0 and num%3==0 and num%5==0):
    print("the number is divisible by all")
elif(num%2==0 and num%3==0):
    print("the number is divisible by 2 and 3")
elif(num%2==0 and num%5==0):
    print("the number is divisible by 2 and 5")
elif(num%3==0 and num%5==0):
    print("the number is divisible by 3 and 5")
elif(num%2==0):
    print("the nuber is divisible by only 2")
elif(num%3==0):
    print("the nuber is divisible by only 3")
elif(num%5==0):
    print("the nuber is divisible by only 5")
else:
    print("invilid input")