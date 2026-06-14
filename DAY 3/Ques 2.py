start = int(input("Enter start: "))
end   = int(input("Enter end: "))

print(f"Prime numbers between {start} and {end}:")
for n in range(start, end + 1):
    if n < 2:
            continue
                is_prime = True
                    for i in range(2, n):
                            if n % i == 0:
                                        is_prime = False
                                                    break
                                                        if is_prime:
                                                                print(n, end=" ")