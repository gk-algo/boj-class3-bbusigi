from collections import defaultdict


if __name__ == "__main__":
    result = []
    for _ in range(int(input())):
        data = defaultdict(int)
        for _ in range(int(input())):
            info = input().split(' ')
            data[info[1]] += 1

        cnt = 1

        for k in data:
            cnt *= (data[k] + 1)
        result.append(cnt)
    for i in result:
        print(i-1)
