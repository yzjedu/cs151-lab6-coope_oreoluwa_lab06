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
