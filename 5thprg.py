# 5) bonas:- Wap that sinmulates game of rock papper and sizer between the two users

user1 = input("user1 choose 'rock','paper','sizer' ")
user2 = input("user2 choose 'rock','paper','sizer' ")
if user1.isdigit() and user2.isdigit():
   print("don't enter number.")
elif user1==user2:
  print("draw")

elif (user1=='rock' and user2 =='sizer') or (user1=='sizer' and user2=='paper') or (user1=='paper' and user2=='rock') :
    print("user1 Win",user1)
else:
    print("user2 win", user2)
