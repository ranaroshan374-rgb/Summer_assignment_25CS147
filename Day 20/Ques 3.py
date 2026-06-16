def row_wise_sum(mat):
        return [sum(row) for row in mat]

        def col_wise_sum(mat):
            n = len(mat)
                m = len(mat[0])
                    return [sum(mat[i][j] for i in range(n))
                                for j in range(m)]

                                def input_matrix(n, m):
                                    return [list(map(int, input(f"Row {i+1}: ").split()))
                                                for i in range(n)]

                                                n    = int(input("Enter rows   : "))
                                                m    = int(input("Enter columns: "))
                                                mat  = input_matrix(n, m)

                                                r_sums = row_wise_sum(mat)
                                                c_sums = col_wise_sum(mat)

                                                print("\nRow-wise Sum:")
                                                for i, s in enumerate(r_sums):
                                                    print(f"  Row {i+1}    = {s}")

                                                    print("\nColumn-wise Sum:")
                                                    for j, s in enumerate(c_sums):
                                                        print(f"  Column {j+1} = {s}")