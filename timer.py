import time
from os import name ,system
while True:
    print("what do you want to do? \n\t1)timer \n\t2)Exit")
    choice = input("your choice :")
    if choice == "1":
        hour = int(input("enter hours :"))
        minutes = int(input("enter minutes :"))
        seconds = int(input("enter seconds :"))
        timer = hour * 3600 + minutes * 60 + seconds
        for n in range(timer, 0, -1):
            print(n)
            time.sleep(1)
            if name == "nt":
                system("cls")
            else:
                system("clear")
    elif choice == "2":
        print("Ending...")
        break
    else:
        print("invalid number")