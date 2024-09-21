def function_to_sort(v):
    return sorted(v)

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort(reverse=True)
    b.sort()

    temp = []
    i, j = 0, n - 1
    k, l = 0, m - 1

    while i <= j:
        if abs(a[i] - b[k]) > abs(a[j] - b[l]):
            temp.append(abs(a[i] - b[k]))
            i += 1
            k += 1
        elif abs(a[i] - b[k]) < abs(a[j] - b[l]):
            temp.append(abs(a[j] - b[l]))
            l -= 1
            j -= 1
        else:
            temp.append(abs(a[j] - b[l]))
            if a[i] > b[i]:
                l -= 1
                j -= 1
            else:
                i += 1
                k += 1

    print(sum(temp))
