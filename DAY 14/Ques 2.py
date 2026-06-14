from collections import Counter

def frequency_analysis(arr, key):
        freq       = Counter(arr)
            total      = len(arr)
                count      = freq[key]
                    percentage = (count / total * 100) if total > 0 else 0
                        return freq, count, percentage

                        arr    = list(map(int, input("Enter elements: ").split()))
                        key    = int(input("Enter element: "))

                        freq, count, pct = frequency_analysis(arr, key)

                        print(f"\n{'─'*40}")
                        print(f"  Array              : {arr}")
                        print(f"  Search Element     : {key}")
                        print(f"  Frequency          : {count}")
                        print(f"  Total Elements     : {len(arr)}")
                        print(f"  Percentage         : {pct:.2f}%")
                        print(f"  Most Common        : {freq.most_common(1)[0]}")
                        print(f"  All Frequencies    : {dict(freq)}")
                        print(f"{'─'*40}")