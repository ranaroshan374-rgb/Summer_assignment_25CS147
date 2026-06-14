n = int(input("Enter a number: "))
original = abs(n)
temp = original
reversed_n = 0
while temp > 0:
    reversed_n = reversed_n * 10 + (temp % 10)
        temp //= 10
        if original == reversed_n:
            print(f"{n} is a Palindrome ✅")
            else:
                print(f"{n} is NOT a Palindrome ❌")