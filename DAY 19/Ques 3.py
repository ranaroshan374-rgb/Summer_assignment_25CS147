def transpose_matrix(matrix):
        """Transpose a matrix (rows become columns and vice versa)."""
            rows = len(matrix)
                cols = len(matrix[0])
                    
                        result = []
                            for j in range(cols):
                                    row = []
                                            for i in range(rows):
                                                        row.append(matrix[i][j])
                                                                result.append(row)
                                                                    return result

                                                                    def print_matrix(matrix, name="Matrix"):
                                                                        print(f"{name}:")
                                                                            for row in matrix:
                                                                                    print(" ", row)
                                                                                        print()