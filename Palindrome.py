def IsPalindrome(s):
    return s == s[::-1]
s =input()
ans = IsPalindrome(s)
if ans:
    print("True")
else:
    print("False")