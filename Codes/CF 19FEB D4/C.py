def sum_of_digits(n):
    sum_digits = 0
    while n > 0:
        sum_digits += n % 10
        n //= 10
    return sum_digits

def precompute_sums(limit):

    cumulative_sums = [0]
    current_sum = 0
    for i in range(1, limit + 1):
        current_sum += sum_of_digits(i)
        cumulative_sums.append(current_sum)
    return cumulative_sums

def main():
    t = int(input())
    max_limit = 1000000  
    sums = precompute_sums(max_limit)

    while t > 0:
        n = int(input())
        total_sum = sums[n]
        print(total_sum)
        t -= 1

if __name__ == "__main__":
    main()
