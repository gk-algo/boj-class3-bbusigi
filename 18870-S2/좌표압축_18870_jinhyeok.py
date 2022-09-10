if __name__ == "__main__":
    N = int(input())
    coors = list(map(int, input().split(' ')))

    d = {c: i for i, c in enumerate(sorted(set(coors)))}

    print(' '.join([str(d[c]) for c in coors]))
