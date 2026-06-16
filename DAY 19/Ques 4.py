def diagonal_sum(mat):
        n         = len(mat)
            primary   = sum(mat[i][i]       for i in range(n))
                secondary = sum(mat[i][n-1-i]   for i in range(n))
                    middle    = mat[n//2][n//2] if n % 2 == 1 else 0
                        return primary, secondary, primary + secondary - middle

                        def input_matrix(n):
                            return [list(map(int, input(f"Row {i+1}: ").split()))
                                        for i in range(n)]

                                        n             = int(input("Enter n: "))
                                        mat           = input_matrix(n)
                                        p, s, total   = diagonal_sum(mat)

                                        print(f"Primary   : {p}")
                                        print(f"Secondary : {s}")
                                        print(f"Total     : {total}")