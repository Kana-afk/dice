import random

a = str(input(" player name:"))
b = ('computer')


def help():
    print("\nCommand list")
    print("z - Take dabt")
    print("x - Put money ;")
    print("c - dice roll;")
debt = 0
cashbox = 0
rate = int(0)

print("For a list of commands, enter w")

while True:
    print("\nMoney: ", debt, "som")
    print("rate: ", rate)
    command = input("Enter command: ")
    if command == 'w':
        help()
    elif command == 'z':
        debt = input("Enter the loan amount: ")
        debt = int(debt)
        print("You have: ", debt, "som")
    elif command == 'x':
        rate = input("Put money: ")
        rate = int(rate)
        if rate > debt:
            print("You don't have that much.")
            rate = 0
        else:
            debt = debt - rate
    elif command == 'c':
        if rate == 0:
            print("Put money.")
        else:
            val1 = random.randrange(1, 6)
            val2 = random.randrange(1, 6)
            sum1 = val1 + val2
            print("\nDropped by", a, ':', sum1)
            val1 = random.randrange(1, 6)

            val2 = random.randrange(1, 6)
            sum2 = val1 + val2
            print("Dropped by ", b, ':', sum2)
            if sum1 == sum2:
                print("Throw it again.")
            elif sum1 > sum2:
                debt = debt + rate * 2
                rate = 0
                print("\nYou win!")
            elif sum1 < sum2:
                rate = 0
                print("\nYou lose...")
    else:
        print("\nNot correct, Try again")        
