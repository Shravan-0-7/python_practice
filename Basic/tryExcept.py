
def atm_system():
    balance = 10000

    print("================================")
    print("       WELCOME TO PYTHON ATM")
    print("================================")

    while True:
        print("\n1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        try:
            choice = int(input("\nEnter your choice: "))

            if choice == 1:
                print("\nYour current balance is: ", balance)

            elif choice == 2:
                amount = float(input("Enter deposit amount: "))

                if amount <= 0:
                    raise ValueError("Amount must be greater than zero.")

                balance += amount
                print("Amount deposited successfully!")

            elif choice == 3:
                amount = float(input("Enter withdrawal amount: "))

                if amount <= 0:
                    raise ValueError("Amount must be greater than zero.")

                if amount > balance:
                    raise ValueError("Insufficient balance!")

                balance -= amount
                print("Withdrawal successful!")

            elif choice == 4:
                print("\nThank you for using Python ATM!")
                break

            else:
                raise ValueError("Invalid menu choice!")

        except ValueError as e:
            print("\nInput Error:", e)

        except KeyboardInterrupt:
            print("\nProgram interrupted by user.")
            break

        except Exception as e:
            print("\nUnexpected Error: ", e)

        else:
            print("Operation completed successfully.")

        finally:
            print("--------------------------------")
            print("ATM Transaction Session Active")
            print("--------------------------------")


atm_system()
