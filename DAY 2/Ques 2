n = int(input("Enter a number: "))
original = n
is_negative = n < 0
n = abs(n)
reversed_n = 0
while n > 0:
    digit = n % 10               # Extract last digit
        reversed_n = reversed_n * 10 + digit  # Build reversed number
            n //= 10                     # Remove last digit
            if is_negative:
                reversed_n = -reversed_n
                print("Reversed number =", reversed_n)