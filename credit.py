"""    
    Problem to Solve
In a filed called credit.py in a folder called sentimental-credit, write a program that prompts the user for a 
credit card number and then reports (via print) whether it is a valid American Express, MasterCard, or Visa card 
number, exactly as you did in Problem Set 1. Your program this time should be written in Python!

    Specification
So that we can automate some tests of your code, we ask that your program's last line of output be AMEX or 
MASTERCARD or VISA or INVALID, nothing more, nothing less.
For simplicity, you may assume that the user's input will be entirely numeric (i.e., devoid of hyphens, as 
might be printed on an actual card).
Best to use get_int or get_string from CS50's library to get users' input, depending on how you to decide to 
implement this one.

    Hints
It's possible to use regular expressions to validate user input. You might use Python's re module, for example, 
to check whether the user's input is indeed a sequence of digits of the correct length.

    How to Test
While check50 is available for this problem, you're encouraged to first test your code on your own for each of 
the following.

> Run your program as python credit.py, and wait for a prompt for input. Type in 378282246310005 and press enter. 
    Your program should output AMEX.
> Run your program as python credit.py, and wait for a prompt for input. Type in 371449635398431 and press enter. 
    Your program should output AMEX.
> Run your program as python credit.py, and wait for a prompt for input. Type in 5555555555554444 and press enter. 
    Your program should output MASTERCARD.
> Run your program as python credit.py, and wait for a prompt for input. Type in 5105105105105100 and press enter. 
    Your program should output MASTERCARD.
> Run your program as python credit.py, and wait for a prompt for input. Type in 4111111111111111 and press enter. 
    Your program should output VISA.
> Run your program as python credit.py, and wait for a prompt for input. Type in 4012888888881881 and press enter. 
    Your program should output VISA.
> Run your program as python credit.py, and wait for a prompt for input. Type in 1234567890 and press enter. 
    Your program should output INVALID.
"""