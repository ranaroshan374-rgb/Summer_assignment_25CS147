n = int(input("Enter a number: "))
temp = n
total = 0
while temp > 0:
    digit = temp % 10       # Extract last digit
        fact = 1
            for i in range(1, digit + 1):
                    fact *= i           # Find factorial of digit
                        total += fact           # Add factorial to total
                            temp //= 10
                            if total == n:
                                print(f"{n} is a Strong Number ✅")
                                else:
                                    print(f"{n} is NOT a Strong Number ❌")