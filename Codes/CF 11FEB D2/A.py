def solve():
    length, width = map(int, input().split())
    half_length, half_width = width, length  
    if length % 2 == 0:
        half_length = length // 2
    if width % 2 == 0:
        half_width = width // 2  
    if half_length != width or half_width != length:
        print("Yes")
    else:
        print("No")

def main():
    test_cases = int(input())
    while test_cases > 0:
        solve()
        test_cases -= 1

if __name__ == "__main__":
    main()
