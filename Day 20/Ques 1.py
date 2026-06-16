def input_matrix(name, rows, cols):
        print(f"Enter {name}:")
            return [list(map(int, input(f"  Row {i+1}: ").split()))
                        for i in range(rows)]

                        def print_matrix(mat, name="Matrix"):
                            print(f"\n{name}:")
                                for row in mat:
                                        print("  ", row)

                                        def multiply(mat1, mat2, r1, c1, c2):
                                            result = [[0] * c2 for _ in range(r1)]
                                                for i in range(r1):
                                                        for j in range(c2):
                                                                    for k in range(c1):
                                                                                    result[i][j] += mat1[i][k] * mat2[k][j]
                                                                                        return result

                                                                                        r1 = int(input("Rows of matrix 1    : "))
                                                                                        c1 = int(input("Columns of matrix 1 : "))
                                                                                        r2 = int(input("Rows of matrix 2    : "))
                                                                                        c2 = int(input("Columns of matrix 2 : "))

                                                                                        if c1 != r2:
                                                                                            print("Error: c1 must equal r2!")
                                                                                            else:
                                                                                                mat1   = input_matrix("Matrix 1", r1, c1)
                                                                                                    mat2   = input_matrix("Matrix 2", r2, c2)
                                                                                                        result = multiply(mat1, mat2, r1, c1, c2)

                                                                                                            print_matrix(mat1, "Matrix 1")
                                                                                                                print_matrix(mat2, "Matrix 2")
                                                                                                                    print_matrix(result, "Result")