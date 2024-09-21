
def most(s):
    count_a = s.count('A')
    count_b = s.count('B')
    if count_a > count_b:
        return 'A'
    elif count_b > count_a:
        return 'B'
    else:  
        return 'A'  


t = int(input())


for _ in range(t):
    string_input = input()
 
    print(most(string_input))
