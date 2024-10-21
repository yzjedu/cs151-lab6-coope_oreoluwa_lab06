# Algorithm Document
#### PLEASE! PLEASE! PLEASE! THINK before you code...

1. Define a function to check if the balance is negative:
   1. If the current balance is less than zero:
      1. Output a warning to the user to say that the balance is negative and they will be charged 5% interest
2. Define a function to check if the withdraw amount is less than zero
   1. If withdrawal amount is less than zero:
      1. Output an error and ask the user to enter a positive number
   2. Otherwise:
      1. Subtract withdrawal amount from the current balance and update the value of current balance
      2. Output that the withdrawal was successful
      3. Output the new balance
3. Define a function to check if the inputted withdrawal amount is a digit
   1. If the withdrawal amount is a digit:
      1. Convert the withdrawal amount to an integer
   2. Otherwise:
      1. Output an error and ask the user to input a valid number
4. Define a function to check if the deposit amount is less than zero
   1. If deposit amount is less than zero:
      1. Output an error and ask the user to enter a positive number
   2. Otherwise:
      1. Add the deposit amount to the current balance and update the value of current balance
      2. Output that the deposit was successful
      3. Output the new balance
5. Define a function to check if the inputted deposit amount is a digit
   1. If the deposit amount is a digit:
      1. Convert the deposit amount to an integer
   2. Otherwise:
      1. Output an error and ask the user to input a valid number
6. Define a function to process the user's choice (deposit, withdraw, view balance, exit)
   1. If the user chooses to deposit:
      1. Call the deposit digit function
   2. Otherwise if the user chooses to view balance:
      1. Output the current balance
   3. Otherwise if the user chooses to withdraw:
      1. Call the withdraw digit function
   4. Otherwise if the user chooses to exit:
      1. Output a thank-you message and a goodbye to the user
   5. Otherwise:
      1. Output that it was an invalid choice and ask the user to input D, W, V, or E
7. Define a function to process the user's decision
   1. While the choice is not equal to the sentinel:
      1. Prompt the user to choose whether they want to deposit, withdraw, view balance, or exit
      2. Call the choice function
8. Define a function for the main program
   1. Output the purpose of the program
   2. Initialize the variables
      * INITIAL_BALANCE = 1000 
      * current_balance = INITIAL_BALANCE 
      * SENTINEL = 'E' 
      * choice = ''
   3. Call the decision function
   4. Output that the program has ended
9. Call the main function

Note: This is streamlined (in a sense)
## Option 2:
1. Define function to display welcome message.
   1. Output "Welcome to the ATM program! This program allows you to interact with your account balance."
2. Define function to display menu options
   1. Output "Please select an option:"
          "D - Deposit"
          "W - Withdraw"
          "V - View Balance"
          "E - Exit"
3. Define function to validate amount:
   1. If amount is a digit:
      1. Convert amount to an integer. 
      2. Return the integer value.
   2. Otherwise:
      1. Print "Error: Please enter a valid number."
      2. Return None.
4. Define function to warn user if the balance is negative
   1. If the current balance is less than 0:
      1. Output "❕ Warning: You have a negative balance. You will be charged 5% interest."
5. Define function to handle deposit process
   1. Prompt the user for the deposit amount. 
   2. Store the user input in deposit_amount. 
   3. Call validate_amount function to validate deposit amount and store the result.
   4. If the deposited amount is not None and is greater than 0:
      1. Add deposited amount to current balance. 
      2. Output new current balance.
   5. Otherwise:
      1. Output "Error: Please enter a positive number."
   6. Return the updated current balance.
6. Define function to handle the withdrawal process
   1. Prompt the user for the withdrawal amount. 
   2. Store the user input in withdraw_amount. 
   3. Call validate_amount function to validate withdrawal amount and store the result. 
   4. If withdraw_amount is not None and is greater than 0:
      1. Subtract withdrawal amount from current balance. 
      2. Output new current balance.
      3. Call check_negative_balance to check for negative balance. 
   5. Otherwise:
      1. Output "Error: Please enter a positive number."
   6. Return the updated current_balance.
7. Define function to view the current balance
   1. Output current balance
8. Define function to process the user's menu choice
   1. If choice is 'D':
      1. Call deposit function and update current balance. 
   2. Otherwise, if choice is 'V':
      1. Call view balance function 
   3. Otherwise, if choice is 'W':
      1. Call withdrawal function and update current balance. 
   4. Otherwise, if choice is 'E':
      1. Output "Thank you for using the ATM program. Goodbye!"
   5. Otherwise:
      1. Output "Error: Invalid choice. Please enter D, W, V, or E."
   6. Return the updated current balance.
9. Define main_function
   1. Call display welcome function. 
   2. Initialize current_balance to 1000. 
   3. Set choice to an empty string. 
   4. While choice is not equal to SENTINEL:
      1. Call the display menu function. 
      2. Prompt the user for input and store in choice. 
      3. Convert choice to uppercase. 
      4. Call process choice function and update current balance. 
      5. Output "ATM program has ended."
10. Call the main function. 
