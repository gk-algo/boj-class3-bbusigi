import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, input().split(' '))

    data = {}
    for num in range(1, N+1):
        name = input().rstrip()
        data[num] = name
        data[name] = num

    a = []
    for _ in range(M):
        q = input().rstrip()
        try:
            num = int(q)
            print(data[num])
        except ValueError:
            print(data[q])
