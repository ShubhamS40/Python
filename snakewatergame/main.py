'''
making simple
snake water gun Game for fun

s=0
w=1
g= -1

'''


import random

computer=random.choice([0,1,-1]);

print("Choose one option :")
print(" Snake : S \n Water : W \n Gun : G");
you=input("Enter the input word :").lower()



list = {
    's': 0,
    'w': 1,
    'g': -1
}

reverselist={
    0:'Snake',
    1:'Water',
    -1:'Gun',
}
youNumber=list[you]

print(f"the computer is choose {reverselist[computer]}")
print(f"You choose {reverselist[youNumber]}")


if(computer==list[you]):
    print("the match is draw")
else:
    if(computer==1 and list[you]==-1): 
     print("you lose!")
    elif(computer==1 and list[you]==0):
     print("you win!")
    elif(computer==0 and list[you]==1):
     print("you lose!")
    elif(computer==-1 and list[you]==1):
      print("you win!")
    elif(computer==0 and list[you]==-1):
      print("you Win!")
    elif(computer==-1 and list[you]==0):
      print("you Win!")
    else:
      print("something went error :")