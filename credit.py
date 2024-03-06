"""    
    Problem to Solve
In a file called credit.py, write a program that prompts the user for a credit card number and then reports (via 
print) whether it is a valid American Express, MasterCard, or Visa card number, exactly as you did in Problem Set 1. 
Your program this time should be written in Python!

        Problem set 1:

            Problem to Solve
        A credit (or debit) card, of course, is a plastic card with which you can pay for goods and services. Printed 
        on that card is a number that's also stored in a database somewhere, so that when your card is used to buy 
        something, the creditor knows whom to bill. There are a lot of people with credit cards in this world, so 
        those numbers are pretty long: American Express uses 15-digit numbers, MasterCard uses 16-digit numbers, and
        Visa uses 13- and 16-digit numbers. And those are decimal numbers (0 through 9), not binary, which means, 
        for instance, that American Express could print as many as 10^15 = 1,000,000,000,000,000 unique cards! 
        (That's, um, a quadrillion.)

        Actually, that's a bit of an exaggeration, because credit card numbers actually have some structure to them. 
        All American Express numbers start with 34 or 37; most MasterCard numbers start with 51, 52, 53, 54, or 55 
        (they also have some other potential starting numbers which we won't concern ourselves with for this problem); 
        and all Visa numbers start with 4. But credit card numbers also have a “checksum” built into them, a 
        mathematical relationship between at least one number and others. That checksum enables computers (or humans 
        who like math) to detect typos (e.g., transpositions), if not fraudulent numbers, without having to query a 
        database, which can be slow. Of course, a dishonest mathematician could certainly craft a fake number that 
        nonetheless respects the mathematical constraint, so a database lookup is still necessary for more rigorous 
        checks.

        In a file called credit.c in a folder called credit, implement a program in C that checks the validity of a 
        given credit card number.

            Luhn's Algorithm
        So what's the secret formula? Well, most cards use an algorithm invented by Hans Peter Luhn of IBM. According 
        to Luhn's algorithm, you can determine if a credit card number is (syntactically) valid as follows:

            1. Multiply every other digit by 2, starting with the number's second-to-last digit, and then add those products' 
            digits together.
            2. Add the sum to the sum of the digits that weren't multiplied by 2.
            3. If the total's last digit is 0 (or, put more formally, if the total modulo 10 is congruent to 0), the number 
            is valid!

        That's kind of confusing, so let's try an example with David's Visa: 4003600000000014.

        For the sake of discussion, let's first underline every other digit, starting with the number's second-to-
        last digit:

        4003600000000014

        Okay, let's multiply each of the underlined digits by 2:
         1•2 + 0•2 + 0•2 + 0•2 + 0•2 + 6•2 + 0•2 + 4•2

        That gives us:
        2 + 0 + 0 + 0 + 0 + 12 + 0 + 8

        Now let's add those products' digits (i.e., not the products themselves) together:
        2 + 0 + 0 + 0 + 0 + 1 + 2 + 0 + 8 = 13

        Now let's add that sum (13) to the sum of the digits that weren't multiplied by 2 (starting from the end):
        13 + 4 + 0 + 0 + 0 + 0 + 0 + 3 + 0 = 20

        Yup, the last digit in that sum (20) is a 0, so David's card is legit!

        So, validating credit card numbers isn't hard, but it does get a bit tedious by hand. Let's write a program.


    Specification
So that we can automate some tests of your code, we ask that your program's last line of output be AMEX or 
MASTERCARD or VISA or INVALID, nothing more, nothing less.

For simplicity, you may assume that the user's input will be entirely numeric (i.e., devoid of hyphens, as 
might be printed on an actual card).

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

import re

def main():
    # While loop to get correct inputs
    while True:
        credit_card_no = input("Please give me a credit card number to assess: ")
        # Regular expression catches as per instructions, any length of digits that is not, 13, 15, 16 in length
        if re.match(r"^(?!.{14}$)[0-9]{13}|[0-9]{15,16}$", credit_card_no): 
            break
        # If incorrect input then message is printed to user and loop repeats
        print("ERROR: input a credit card number of 13, 15 or 16 digits")
    
    # Two variables are used with specific names for their intention These variables count backwards from the 
    #   end of the string and step over 1 char as per Luhm's algorithm (line 31-62)
    second_to_last_digit = credit_card_no[-2::-2]
    last_digit = credit_card_no[::-2]
    
    output = ''

    # Regular expressions then look at the beginning of the inputed credit card no. Depending on how they begin
    #   determines what Company they belong too. See lines 18-21. If valid then result is saved in output
    if re.match(r"^3[4-7][0-9]*$", credit_card_no):
        output = "AMEX"
    elif re.match(r"^4[0-9]*$", credit_card_no):
        output = "VISA"
    elif re.match(r"^5[1-5][0-9]*$", credit_card_no):
        output = "MASTERCARD"
    # If they do not match any of the above companies then it must be invalid
    else:
        return "Invalid"

    total = 0

    # First for loop goes through the second to last digit list, which per Luhm's algorithm must be multiplied by
    #   2, then added to a total. If the reult is larger than 9, then the numbers must be split, 12, becomes 1+2.
    #   Therefore the output is saved as a string in temp, then split and turned into numbers and added to the total. 
    for digit in second_to_last_digit:
        temp = ''
        if int(digit) * 2 > 9:
            temp = str(int(digit) * 2)
            total += int(temp[0]) + int(temp[1]) 
        else:
            total += int(digit) * 2

    # Second loop just adds the numbers from the last digit to the total
    for digit in last_digit:
        total += int(digit)
    
    # According to luhm, if the resulting number ends with a 0, like 20, 30 etc, then the credit card number is 
    #   legitimate, and returns the correct credit card company the number belongs to that was sorted earlier. 
    #   Otherwise return Invalid.
    if str(total)[-1] == "0":
        return output
    else:
        return "Invalid"
    
print(main())