from collections import defaultdict

s    = input("Enter a string: ")
freq = defaultdict(int)

for ch in s:
    freq[ch] += 1

    print("\nCharacter Frequency:")
    for ch in sorted(freq):
        print(f"  '{ch}' → {freq[ch]}")