def test_case():
    n = int(input())
    s1 = input()
    s2 = input()
    cnt1 = 0
    cnt2 = 0

    for i in range(n):
        if s1[i] == '0' and s1[i] != s2[i]:
            cnt1 += 1
        if s2[i] == '0' and s2[i] != s1[i]:
            cnt2 += 1

    print(max(cnt1, cnt2))


def main():
    t = int(input())
    for _ in range(t):
        test_case()


if __name__ == "__main__":
    main()

