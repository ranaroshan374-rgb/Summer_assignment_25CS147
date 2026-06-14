def fibonacci(n, memo={}):
        if n in memo:
                    return memo[n]          # Return cached result
                        if n == 0: return 0
                            if n == 1: return 1
                                memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
                                    return memo[n]

                                    n = int(input("Enter number of terms: "))
                                    print("Fibonacci Series:")
                                    for i in range(n):
                                            print(fibonacci(i), end=" ")