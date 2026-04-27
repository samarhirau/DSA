# Problem: Valid Palindrome

# Question:
# Check if a string is a palindrome (ignore non-alphanumeric, case insensitive)

def is_palindrome(s):
    left, right = 0, len(s) - 1
    
    while left < right:
        if not s[left].isalnum():
            left += 1
        elif not s[right].isalnum():
            right -= 1
        elif s[left].lower() != s[right].lower():
            return False
        else:
            left += 1
            right -= 1
    
    return True



s = "A man, a plan, a canal: Panama"
print(is_palindrome(s))