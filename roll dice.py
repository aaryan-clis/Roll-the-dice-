import random   

def rolldice(min, max):
    while true :
      print("Rolling dice....")
    number = random.randint(min, max)
    print(f"your number :{random.randint(min, max)}")
    choice = input("do you want to roll the dice again ? (y/n)")



    rolldice(1, 6)