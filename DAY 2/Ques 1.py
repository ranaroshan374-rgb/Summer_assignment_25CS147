n = int(input("Enter a number: "))
n = abs(n)
total = 0
while n > 0:
    total += n % 10   # Extract last digit
        n //= 10          # Remove last digit
        print("Sum of digits =", total)