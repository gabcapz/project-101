import random




def roll_a_dice(response):
    again = input("Type yes to roll again:")
    while response or again == "yes":
        no = random.randint(1, 6)
        if (no == 1):
          print("0", end='\r')
         # print(again, end='\r')
        if (no == 2):
          print("0 0", end='\r') 
         # print(again, end='\r')
        if (no == 3):
          print("0 0 0", end='\r')     
          #print(again, end='\r')
        if (no == 4):
          print("0 0 0 0", end='\r')
         # print(again, end='\r') 
        if (no == 5):
          print("0 0 0 0 0", end='\r') 
          #print(again, end='\r')
        if (no == 6):
          print("0 0 0 0 0 0", end='\r') 
          #print(again, end='\r')

  

roll = input("Do you want to roll a dice?")
response = "yes"

roll_a_dice(response)
 
