#1935 Maximum Number of Words You can Type

def canBeTypedWords(text, brokenLetters):
    i = 0
    brokenLetterList = [char for char in brokenLetters]
    for word in text.split():
        if not any(ch in brokenLetterList for ch in word):
            i += 1
    return i

"""
print(canBeTypedWords("hello world", "ad"))
print(canBeTypedWords("leet code", "lt"))
print(canBeTypedWords("leet code", "e"))
"""
#2. Add Two Numbers (Failed)

def addTwoNumbers(l1, l2):
    num1 = int("".join(str(x) for x in l1))
    num2 = int("".join(str(y) for y in l2))

    output_string = [int(x) for x in str(num1 + num2)][::-1]

    return output_string

#print(addTwoNumbers([2,4,3], [5,6,4]))

#9. Palindrome Number

def isPalindrome(x):
    if x < 0:
        return False
    
    x_list = [int(y) for y in str(x)]

    if x_list == x_list[::-1]:
        return True
    else:
        return False
    
print(isPalindrome(121))
print(isPalindrome(-121))

#13. Roman to Integer

def romanToInt(s):
    total = 0
    reverse_s = s[::-1]

    for idx in range(len(reverse_s)):
        current = reverse_s[idx]
        nxt = reverse_s[idx - 1] if idx - 1 >= 0 else None

        if current == "I":
            total += 1 if nxt != "V" and nxt != "X" else -1
        elif current == "V":
            total += 5
        elif current == "X":
            total += 10 if nxt not in ("L", "C") else -10
        elif current == "L":
            total += 50
        elif current == "C":
            total += 100 if nxt not in ("D", "M") else -100
        elif current == "D":
            total += 500
        elif current == "M":
            total += 1000

    return total


print(romanToInt("LVIII"))
        