import re
def isvalid(s):
    pattern =re.compile("^[\+\s.\-\/d\)]{5,30}$")
s="+12124567890"
s1="+212-456-7890"
s2="1-212-456-7890"
s4="+1 212.456.7890"
s5="(212)-456-7890"

if(isvalid(s)):
    print("valid number")
else:
    print("invalid number")

output:invalid number


