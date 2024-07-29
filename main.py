import random

'''
1:rock 
2:paper
3:Scissors
'''
print("---------------------------------------------------------")
print("Welcome to Rock-Papaer-Scissors Game v0.1 :) !!!!")

while True:
    flag = 0
    computer=random.choice([1,2,3])
    print("---------------------------------------------------------")
    yours=input("Enter your Choice: Rock|Paper|Scissors -->")
    yourdict={"rock":1,"paper":2,"scissors":3}
    reverdict={1:"Rock",2:"Paper",3:"Scissors"}
    shortformdict={"r":"rock","p":"paper","s":"scissors"}
    yours=yours.lower()
    if(yours!="rock" and yours!="paper" and yours!="scissors"):
        print("!!! Please only enter Rock|Paper|Scissors")
        continue

    you=yourdict[yours]

    print(f"You have choose -->{reverdict[you]} \nComputer have choose -->{reverdict[computer]}")

    if(computer == you):
        print("Its a draw !!")
    else:
        if(computer ==1 and you == 2):
            print("Congratulations you win !!")    
        elif(computer ==1 and you == 3):
            print("Sorry you loss !!")  
        elif(computer ==2 and you == 1):
            print("Sorry you loss !!!") 
        elif(computer ==2 and you == 3):
            print("Congratulations you win !!")    
        elif(computer ==3 and you == 1):
            print("Congratulations you win !!")  
        elif(computer ==3 and you == 2):
            print("Sorry you loss !!!")
        else:
            print("Someting went wrong") 
    print("---------------------------------------------------------")         
    flag=int(input("Enter 1 to play again | Enter 2 for Exit the Game ->"))
    if(flag == 2):
        print("Bye !!! come back soon !!!")
        break                   