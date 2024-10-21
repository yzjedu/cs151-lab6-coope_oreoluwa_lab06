# Programmers:  [your name here]
# Course:  CS151, [Instructors name here]
# Due Date: [date assignment is due]
# Programming Assignment:  [number of assignment]
# Problem Statement:  [what problem does your code solve; i.e., calculating inches from centimeters]
# Data In: [what information do you request from the user?]
# Data Out:  [What information do you display for the user?]
# Credits: [Is your code based of an example in the book, in class, or something else?  Reminder: you should never take code from the Internet or another person.]


# Function to display the welcome message
def display_welcome():
    print("Welcome to the ATM program! This program allows you to interact with your account balance.")


# Function to display the menu options
def display_menu():
    print("\nPlease select an option:"
          "\n\t D - Deposit"
          "\n\t W - Withdraw"
          "\n\t V - View Balance"
          "\n\t E - Exit")


# Function to validate if the input amount is a digit
def validate_amount(amount):
    if amount.isdigit():
        return int(amount)
    else:
        print("Error: Please enter a valid number.")
        return None


# Function to check if the balance is negative
def check_negative_balance(current_balance):
    if current_balance < 0:
        print("❕ Warning: You have a negative balance. You will be charged 5% interest.")


# Function to handle the deposit process
def deposit(current_balance):
    deposit_amount = input("Enter the amount to deposit: ").strip()
    deposit_amount = validate_amount(deposit_amount)
    if deposit_amount is not None and deposit_amount > 0:
        current_balance += deposit_amount
        print(f"Deposit successful! Your new balance is ${current_balance:.2f}.")
    return current_balance

# Function to handle the withdrawal process
def withdraw(current_balance):
    withdraw_amount = input("Enter the amount to withdraw: ").strip()
    withdraw_amount = validate_amount(withdraw_amount)

    if withdraw_amount is not None and withdraw_amount > 0:
        current_balance -= withdraw_amount
        print(f"Withdrawal successful! Your new balance is ${current_balance:.2f}.")
        check_negative_balance(current_balance)
    return current_balance


# Function to display the current balance
def view_balance(current_balance):
    print(f"Your current balance is ${current_balance:.2f}.")


# Function to process the user's menu choice
def process_choice(choice, current_balance):
    if choice == 'D':
        current_balance = deposit(current_balance)
    elif choice == 'V':
        view_balance(current_balance)
    elif choice == 'W':
        current_balance = withdraw(current_balance)
    elif choice == 'E':
        print("Thank you for using the ATM program. Goodbye!")
    else:
        print("Error: Invalid choice. Please enter D, W, V, or E.")
    return current_balance


# Main function to run the ATM program
def atm_program():
    display_welcome()
    # Initialize variables
    INITIAL_BALANCE = 1000
    current_balance = INITIAL_BALANCE
    SENTINEL = 'E'
    choice = ''

    while choice.upper() != SENTINEL:
        display_menu()
        choice = input("Your choice: ").strip().upper()
        current_balance = process_choice(choice, current_balance)

    print("ATM program has ended.")


# Start the ATM application
atm_program()