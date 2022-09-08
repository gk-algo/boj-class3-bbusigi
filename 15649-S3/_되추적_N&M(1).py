#N, M = map(int,input().split())
# N 은 1 ~ N
# M은 개수


N = 4 ; M=2

global visited
visited = [0 for _ in range(N)]
s = []

def DFS():
    if len(s) == M:
        print(' '.join(map(str,s)))
        return
    
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            s.append(i+1)
            DFS()
            s.pop()
            visited[i] = False

DFS()