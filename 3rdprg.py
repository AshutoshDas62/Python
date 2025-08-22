# 3)  WAP the take three nos of input from the user and print the 2nd larges among them

a = int(input("enter 1st no. "))
b = int(input("enter 2nd no. "))
c = int(input("enter 3rd no. "))
d = int(input("enter 4th no. "))
   
   # method_1
   
# if a>=b and b>=c:
#     if b>=c:
#         print("second largest", b)
# elif b>=c and c>=a:
#     if b>=c:
#         print("second largest", c)
# else:
#     print("second largest", a)
   
   # method_2
   
nums=[a,b,c,d]
nums.sort() # accending order
print("the sorted numbers are : ", nums)
print("the second largest no. :", nums[-2])

nums.sort(reverse=True)   # decending order
print("the sorted numbers are : ", nums)
print("the second largest no. :", nums[1])
