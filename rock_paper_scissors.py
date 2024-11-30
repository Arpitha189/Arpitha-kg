import random
you=int(input("enter the number 0 for rock,1 for paper, 2 for scissor:"))
computer=random.randint(0,2)
print(computer)
if(you==computer):
   print("it is a draw")
if(you==0 and computer==2):
   print("you won")
if(you==2 and computer==0):
   print("you lose")
if(you>2 or you<0):
  print("invalid try again...")   
elif(you>computer):
  print("you won") 
elif(computer>you):
  print("you lose")   