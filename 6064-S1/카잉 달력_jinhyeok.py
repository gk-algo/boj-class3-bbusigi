import sys
input = sys.stdin.readline

if __name__ == "__main__":
    for _ in range(int(input())):
        M, N, x, y = map(int, input().split(' '))
        
        num = x
        _flag = False
        while num <= M * N:
            if (num - y) % N == 0:
                print(num)
                _flag = True
                break
            num += M
        if not _flag:
            print(-1)
