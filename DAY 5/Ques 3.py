import math

n = int(input("Enter a number: "))
factors = []
for i in range(1, int(math.sqrt(n)) + 1):
    if n % i == 0:
            factors.append(i)           # Add smaller factor
                    if i != n // i:
                                factors.append(n // i)  # Add paired larger factor
                                factors.sort()
                                print(f"Factors of {n}:", *factors)