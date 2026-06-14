n = int(input("Enter a number: "))
original = n
largest  = -1

# Step 1: Divide out all 2s
while n % 2 == 0:
    largest = 2
        n //= 2

        # Step 2: Check odd factors from 3
        i = 3
        while i * i <= n:
            while n % i == 0:
                    largest = i
                            n //= i
                                i += 2

                                # Step 3: If n > 1, then n itself is a prime factor
                                if n > 1:
                                    largest = n

                                    print("Largest Prime Factor =", largest)