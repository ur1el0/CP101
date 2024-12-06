print("WELCOME TO BDO")
print()
print("How may I help you?")
print()

name = input("Enter Account Name: ")
acct = int(input("Please Select an Account (1 for Checking, 2 for Savings): "))
print()
bal = 0

if acct == 1:
    print("Opening Checking Account...")
    print()
    print("Done!")
    print()
    print(f"Hello {name}, your checking account has now been opened...")
    print()
    
    if bal == 0:
        amount = int(input("Your balance is insufficient. How much would you like to deposit? "))
        print()
        bal += amount
        print(f"Your balance is {bal}")
    
    while True:
        print("\nWhat would you like to do now?")
        action = int(input("Please Select: [1] Deposit [2] Withdraw [3] Exit: "))
        
        if action == 1:
            amount = int(input("Enter the amount you want to deposit: "))
            bal += amount
            print(f"Your balance is now {bal}")
        elif action == 2:
            amount = int(input("Enter the amount you want to withdraw: "))
            if amount > bal:
                print("Insufficient balance!")
            else:
                bal -= amount
                print(f"Your balance is now {bal}")
        elif action == 3:
            print("Thank you for banking with BDO!")
            break
        else:
            print("Invalid selection. Please try again.")

elif acct == 2:
    print("Opening Savings Account...")
    print()
    print("Done!")
    print()
    print(f"Hello {name}, your savings account has now been opened...")
    print()
    
    if bal == 0:
        amount = int(input("Your balance is insufficient. How much would you like to deposit? "))
        print("For every deposit, 1% will be deducted.")
        print()
        bal += amount * 0.99
        print(f"Your balance is {bal:.2f}")
    
    while True:
        print("\nWhat would you like to do now?")
        action = int(input("Please Select: [1] Deposit [2] Withdraw [3] Exit: "))
        
        if action == 1:
            amount = int(input("Enter the amount you want to deposit: "))
            bal += amount * 0.99
            print(f"Your balance is now {bal:.2f}")
        elif action == 2:
            amount = int(input("Enter the amount you want to withdraw: "))
            if amount > bal:
                print("Insufficient balance!")
            else:
                bal -= amount
                print(f"Your balance is now {bal:.2f}")
        elif action == 3:
            print("Thank you for banking with BDO!")
            break
        else:
            print("Invalid selection. Please try again.")
else:
    print("Invalid account type selected.")

print(f"Thank you, {name}!")
