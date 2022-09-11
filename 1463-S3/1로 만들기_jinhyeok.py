import sys
input = sys.stdin.readline

if __name__=="__main__":
    number = int(input())
    memo = [0] * (number+1)

    for i in range(2, number+1):
        memo[i] = memo[i-1] + 1

        if i % 3 == 0:
            memo[i] = min(memo[i], memo[i // 3] + 1)
        if i % 2 == 0:
            memo[i] = min(memo[i], memo[i // 2] + 1)
    print(memo[number])
