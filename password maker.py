import random, string
lower = string.ascii_lowercase
upper = string.ascii_uppercase
numb = "0123456789"
symbols = "!@#$%^&*()_+-={}[]/\\<>.,;:'\"|"
all = lower + upper + numb + symbols
while True:
    print("What do you want to do?\n\t1)Make a password \n\t2)Exit")
    choice = input("Your choice?")
    if choice == "1":
        length = int(input("What is the length of your password? "))
        password = "".join(random.sample(all, length))
        print(password)
        print("%" * 30)
    elif choice == "2":
        print("Bye")
        break
    else:
        print("Wrong input")
        print("%" * 30)