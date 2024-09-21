
def lss(t, test_cases):
    results = []
    for test in test_cases:
        n = test[0]
        spell = test[1]
        
     
        i = 0
        while i < n and spell[i] == 'a':
            i += 1
        
        if i == n:
        
            results.append(spell[:-1])
        elif i == 0:
            
            results.append(spell[1:])
        else:
            
            results.append(spell[:i] + spell[i+1:])
    
    return results

t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    spelled = input()
    test_cases.append((n, spelled))


output = lss(t, test_cases)
for result in output:
    print(result)
