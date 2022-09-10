if __name__ == "__main__":
    N, M = map(int, input().split(' '))

    names = []
    for i in range(N):
        names.append(input())

    a = []
    for _ in range(M):
        q = input()
        try:
            num = int(q)
            a.append(names[num-1])
        except ValueError:
            a.append(names.index(q)+1)

    for i in a:
        print(i)
