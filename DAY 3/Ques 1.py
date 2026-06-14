n = int(input("Enter a number: "))
if n < 2:
    print(f"{n} is NOT Prime ❌")
    else:
        is_prime = True
            for i in range(2, n):
                    if n % i == 0:
                                is_prime = False
                                            break
                                                if is_prime:
                                                        print(f"{n} is Prime ✅")
                                                            else:
                                                                    print(f"{n} is NOT Prime ❌")