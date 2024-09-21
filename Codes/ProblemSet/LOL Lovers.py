def find_division(n, items):
    loaves = items.count('L')
    onions = items.count('O')
    
    if loaves == 1 or onions == 1 or loaves == n or onions == n:
        return -1
    
    for i in range(n-1):
        prefix = items[:i+1]
        suffix = items[i+1:]
        if prefix.count('L') != suffix.count('L') and prefix.count('O') != suffix.count('O'):
            return i+1
    
    return -1
 
n = int(input())
items = input()
 
result = find_division(n, items)
print(result)