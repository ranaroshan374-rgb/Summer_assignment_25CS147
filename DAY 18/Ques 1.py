def bubble_sort(arr, descending=False):
        n   = len(arr)
            arr = arr.copy()        # Don't modify original

                for i in range(n - 1):
                        swapped = False
                                for j in range(n - i - 1):
                                            condition = (arr[j] < arr[j+1]
                                                                    if descending
                                                                                            else arr[j] > arr[j+1])
                                                                                                        if condition:
                                                                                                                        arr[j], arr[j+1] = arr[j+1], arr[j]
                                                                                                                                        swapped = True
                                                                                                                                                if not swapped:
                                                                                                                                                            break
                                                                                                                                                                return arr

                                                                                                                                                                arr = list(map(int, input("Enter elements: ").split()))
                                                                                                                                                                print("Ascending :", bubble_sort(arr))
                                                                                                                                                                print("Descending:", bubble_sort(arr, descending=True))