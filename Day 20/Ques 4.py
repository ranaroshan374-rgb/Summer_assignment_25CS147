n   = int(input("Enter rows   : "))
m   = int(input("Enter columns: "))
mat = [list(map(int, input(f"Row {i+1}: ").split()))
       for i in range(n)]

       r_sums = [sum(row) for row in mat]
       c_sums = [sum(col) for col in zip(*mat)]

       print(f"\n{'─'*45}")
       print(f"  Matrix ({n}×{m}):")
       for i, row in enumerate(mat):
           print(f"    Row {i+1}: {row} → Sum = {r_sums[i]}")
           print(f"\n  Column Sums:")
           for j, s in enumerate(c_sums):
               print(f"    Col {j+1}: {s}")
               print(f"\n  Total Sum : {sum(r_sums)}")
               print(f"  Max Row   : Row {r_sums.index(max(r_sums))+1}"
                     f" = {max(r_sums)}")
                     print(f"  Max Col   : Col {c_sums.index(max(c_sums))+1}"
                           f" = {max(c_sums)}")
                           print(f"{'─'*45}")