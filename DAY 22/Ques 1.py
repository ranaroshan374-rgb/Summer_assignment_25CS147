s     = input("Enter a string: ").strip()
left  = 0
right = len(s) - 1

is_palindrome = True
while left < right:
    if s[left] != s[right]:
            is_palindrome = False
                    break
                        left  += 1
                            right -= 1

                            print(f"'{s}' is {'a Palindrome ✅' if is_palindrome else 'NOT a Palindrome ❌'}")