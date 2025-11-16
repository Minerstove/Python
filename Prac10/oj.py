def longest_palindrome_substr(string):
    if type(string) != str:
        raise ValueError
    
    n = len(string)
    l = r = 0

    for i in range(1, n - 1):
        mirror = l + r - i
    
    
#Manacher's algorithm for longest palindromic substyring