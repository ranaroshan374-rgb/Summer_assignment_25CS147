from collections import Counter

def find_duplicates(arr):
        freq         = Counter(arr)
            duplicates   = {k: v for k, v in freq.items() if v > 1}
                unique       = [k for k, v in freq.items() if v == 1]
                    dup_indices  = {}

                        for i, num in enumerate(arr):
                                    if num in duplicates:
                                                    if num not in dup_indices:
                                                                        dup_indices[num] = []
                                                                                    dup_indices[num].append(i)

                                                                                        return duplicates, unique, dup_indices

                                                                                        arr = list(map(int, input("Enter elements: ").split()))
                                                                                        duplicates, unique, indices = find_duplicates(arr)

                                                                                        print(f"\n{'─'*45}")
                                                                                        print(f"  Array            : {arr}")
                                                                                        print(f"  Duplicates       : {list(duplicates.keys())}")
                                                                                        print(f"  Duplicate counts : {dict(duplicates)}")
                                                                                        print(f"  Duplicate indices: {dict(indices)}")
                                                                                        print(f"  Unique elements  : {unique}")
                                                                                        print(f"  Total duplicates : {len(duplicates)}")
                                                                                        print(f"{'─'*45}")