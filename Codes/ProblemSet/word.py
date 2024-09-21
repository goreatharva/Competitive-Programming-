s = input()
upperCount = 0
lowerCount = 0
UPPERCASESTRING = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in s:
    if i in UPPERCASESTRING:
        upperCount += 1
    else:
        lowerCount += 1
        
if upperCount > lowerCount:
    s = s.upper()
else:
    s = s.lower()
    
print(s)