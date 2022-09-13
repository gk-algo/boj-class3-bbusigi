import sys
sys.setrecursionlimit(10**7)

## 함수
def BFS():
    pass

def DFS(x,ans):
    temp_list = []
    visited[x-1] = 1 # 방문처리
    if 0 in visited: # 방문안한 노드가 있을 경우
        temp_list = ans
        temp_list.append(x+1)
        for idx in range(N):
            if graph[x-1][idx] == 1 and visited[idx] == 0: # 연결되어 있고 방문안한 노드인경우
                DFS(idx,temp_list)

        
                
    else:
        print(ans) # 안되는중 해결 필요.
        temp_list = ans
        if len(temp_list) == 4:
            print( i + " " for i in temp_list)
            
## main

if __name__ == '__main__':
    # N 정점 개수 (1<=N<=1000)
    # 간선의 개수 (1<=M<=10000)
    # 탐색을 시작할 정점의 번호 V
    temp = []
    N , M , V = map(int,input().split())

    visited = [0]*N

    graph = [[0 for _ in range(N)] for _ in range(N)]

    for _ in range(M):
        X,Y = map(int,input().split())
        graph[X-1][Y-1] = 1
        graph[Y-1][X-1] = 1

    DFS(V,temp)
