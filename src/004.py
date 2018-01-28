def isPalindrome(number):
    strValue = str(number)
    strReverse = strValue[::-1]
    if strValue == strReverse:
        return True
    return False
palindrome = 0
for i in range(999, 0, -1):
    for j in range(i, 0, -1):
        if isPalindrome(i*j):
            if i*j > palindrome:
                palindrome = i*j
print(palindrome)