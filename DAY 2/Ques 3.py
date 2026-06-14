n = int(input("Enter a number: "))
n = abs(n)
product = 1
while n > 0:
    product *= n % 10   # Multiply last digit
        n //= 10            # Remove last digit
        print("Product of digits =", product)