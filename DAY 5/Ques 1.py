import math

n = int(input("Enter a number: "))
if n < 2:
    print(f"{n} is NOT a Perfect Number ❌")
    else:
        total = 1             # 1 is always a divisor
            for i in range(2, int(math.sqrt(n)) + 1):
                    if n % i == 0:
                                total += i
                                            if i != n // i:
                                                            total += n // i
                                                                if total == n:
                                                                        print(f"{n} is a Perfect Number ✅")
                                                                            else:
                                                                                    print(f"{n} is NOT a Perfect Number ❌")