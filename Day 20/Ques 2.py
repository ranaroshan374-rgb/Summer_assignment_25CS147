import numpy as np

def check_symmetric_full(mat):
    n            = len(mat)
        transpose    = [[mat[j][i] for j in range(n)]
                            for i in range(n)]
                                mismatches   = []

                                    for i in range(n):
                                            for j in range(i + 1, n):
                                                        if mat[i][j] != mat[j][i]:
                                                                        mismatches.append(
                                                                                            (i, j, mat[i][j], mat[j][i]))

                                                                                                is_symmetric = len(mismatches) == 0

                                                                                                    # Additional matrix properties
                                                                                                        diagonal     = [mat[i][i] for i in range(n)]
                                                                                                            diag_sum     = sum(diagonal)
                                                                                                                trace        = diag_sum

                                                                                                                    return {
                                                                                                                            "matrix"       : mat,
                                                                                                                                    "transpose"    : transpose,
                                                                                                                                            "is_symmetric" : is_symmetric,
                                                                                                                                                    "mismatches"   : mismatches,
                                                                                                                                                            "diagonal"     : diagonal,
                                                                                                                                                                    "trace"        : trace,
                                                                                                                                                                            "size"         : n
                                                                                                                                                                                }

                                                                                                                                                                                n   = int(input("Enter n: "))
                                                                                                                                                                                mat = [list(map(int, input(f"Row {i+1}: ").split()))
                                                                                                                                                                                       for i in range(n)]

                                                                                                                                                                                       r   = check_symmetric_full(mat)

                                                                                                                                                                                       print(f"\n{'─'*50}")
                                                                                                                                                                                       print(f"  Matrix:")
                                                                                                                                                                                       for row in r['matrix']:
                                                                                                                                                                                           print(f"    {row}")
                                                                                                                                                                                           print(f"  Transpose:")
                                                                                                                                                                                           for row in r['transpose']:
                                                                                                                                                                                               print(f"    {row}")
                                                                                                                                                                                               print(f"  Symmetric      : {'✅ Yes' if r['is_symmetric'] else '❌ No'}")
                                                                                                                                                                                               print(f"  Diagonal       : {r['diagonal']}")
                                                                                                                                                                                               print(f"  Trace          : {r['trace']}")
                                                                                                                                                                                               if not r['is_symmetric']:
                                                                                                                                                                                                   print(f"  Mismatches:")
                                                                                                                                                                                                       for i, j, v1, v2 in r['mismatches']:
                                                                                                                                                                                                               print(f"    mat[{i}][{j}]={v1} ≠"
                                                                                                                                                                                                                             f" mat[{j}][{i}]={v2}")
                                                                                                                                                                                                                             print(f"{'─'*50}")