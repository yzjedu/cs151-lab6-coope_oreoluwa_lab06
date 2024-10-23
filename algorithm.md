# Algorithm Document

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


