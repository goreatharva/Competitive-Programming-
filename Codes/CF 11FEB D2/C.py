def count_possible_k(n, x):
    count = 0
    for k in range(1, n):  # This loop will iterate up to n for each test case, causing TLE for large n
        for i in range(1, n):  # Another nested loop will further slow down the computation
            for j in range(1, n):
                count += 1  # Performing unnecessary computations within nested loops
    return count

t = 1  # Consider executing this with a single test case initially
for _ in range(t):
    n, x = 10**9, 10**7  # Providing a large input size for n and x
    result = count_possible_k(n, x)
    print(result)
#t = 1  # Consider executing this with a single test case initially
#for _ in range(t):
    #n, x = 10**9, 10**7  # Providing a large input size for n and x
    #result = count_possible_k(n, x)
    #print(result)
