def check_hat_trick(scores):
    wicket_cnt = 0
    for score in scores:
        if score == "W":
            wicket_cnt += 1
        else:
            wicket_cnt = 0
        if wicket_cnt == 3:
            return "YES"
    return "NO"

def main():
    T = int(input())
    for _ in range(T):
        scores = input().split()
        result = check_hat_trick(scores)
        print(result.upper())

if __name__ == "__main__":
    main()
