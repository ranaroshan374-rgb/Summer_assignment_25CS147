def add_matrices(matrix1, matrix2):
        """Add two matrices of the same dimensions."""
            rows = len(matrix1)
                cols = len(matrix1[0])
                    
                        result = []
                            for i in range(rows):
                                    row = []
                                            for j in range(cols):
                                                        row.append(matrix1[i][j] + matrix2[i][j])
                                                                result.append(row)
                                                                    return result

                                                                    def print_matrix(matrix, name="Matrix"):
                                                                        print(f"{name}:")
                                                                            for row in matrix:
                                                                                    print(" ", row)
                                                                                        print()
                                                                       
    
                                    
                                    
                                            
