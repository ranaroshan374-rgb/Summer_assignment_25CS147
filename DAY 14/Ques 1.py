def linear_search(arr, key):
        for i in range(len(arr)):
                    if arr[i] == key:
                                    return i          # Return index if found
                                        return -1                 # Return -1 if not found

                                        arr = list(map(int, input("Enter elements: ").split()))
                                        key = int(input("Enter element to search: "))

                                        result = linear_search(arr, key)
                                        if result != -1:
                                                print(f"Element {key} found at index {result}")
                                                else:
                                                        print(f"Element {key} not found ❌")