s=input("Enter string name:")
def ispalindrome(s):
    rev = ''.join(reversed(s))
    if(s==rev):
        return True
    return False
ans = ispalindrome(s)
if(ans):
    print("Yes")
else:
    print("No")
