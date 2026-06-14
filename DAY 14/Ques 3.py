def find_largest_elements(arr):
        if len(arr) < 2:
                    return "Need at least 2 elements"

                        largest = second = third = float('-inf')

                            for num in arr:
                                        if num > largest:
                                                        third   = second
                                                                    second  = largest
                                                                                largest = num
                                                                                        elif num > second and num != largest:
                                                                                                        third  = second
                                                                                                                    second = num
                                                                                                                            elif num > third and num != second:
                                                                                                                                            third  = num

                                                                                                                                                return largest, second, third

                                                                                                                                                arr = list(map(int, input("Enter elements: ").split()))
                                                                                                                                                l, s, t = find_largest_elements(arr)

                                                                                                                                                print(f"\n{'─'*35}")
                                                                                                                                                print(f"  Array          : {arr}")
                                                                                                                                                print(f"  Largest        : {l}")
                                                                                                                                                print(f"  Second Largest : {s}")
                                                                                                                                                print(f"  Third Largest  : {t}")
                                                                                                                                                print(f"{'─'*35}")