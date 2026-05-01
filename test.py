ask = int(input("Enter an amount: "))
ask2 = int(input("Enter another amount: "))

def addition():
    print(ask + ask2)

def subtraction():
    if ask > ask2:
        print(ask - ask2)
    elif ask < ask2:
        print(ask2 - ask)

def multiplication():
    print(ask * ask2)

def division():
    if ask > ask2:
        print(ask / ask2)
    elif ask < ask2:
        print(ask2 / ask)


choice = input("Addition(a) Subtraction(s) Division(d) Multiplication(m): ")
if choice == 'a':
    addition()
elif choice == 's':
    subtraction()
elif choice == 'd':
    division()
elif choice == 'm':
    multiplication()
