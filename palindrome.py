

# Palindrome Checking 
def plaindromecheck(text):
    left =0
    right = len(text) - 1
    while left < right:
        if text[right] != text[left]: 
            return False
        else:
            return True
        left += 1
        right -= 1

print(plaindromecheck('lloaoll')) 