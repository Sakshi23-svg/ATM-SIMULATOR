balance = 1000

print("Welcome to ATM")

while True:
    print("\n1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Your balance is:", balance)

    elif choice == "2":
        deposit = int(input("Enter amount to deposit: "))
        balance = balance + deposit
        print("Money deposited successfully")

    elif choice == "3":
        withdraw = int(input("Enter amount to withdraw: "))

        if withdraw <= balance:
            balance = balance - withdraw
            print("Please collect your cash")
        else:
            print("Insufficient balance")

    elif choice == "4":
        print("Thank you for using ATM")
        break

    else:
        print("Invalid choice")
