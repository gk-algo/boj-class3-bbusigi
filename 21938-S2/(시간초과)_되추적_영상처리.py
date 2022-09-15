import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def _comp(graph):
    global _not_visited
    # RGB 평균이 T를 넘을 경우 255 출력 함수
    promising = lambda T,idx,input_list : 255 if sum(input_list[3*idx:3*(idx+1)]) >= T else 0
    # 255 인 애들의 상하좌우 확인
    # 255끼리 붙어있으면 동일 물체

    # 전처리 된 graph 값
    comp_graph = []
    for row in range(N):
        temp = []
        for idx in range(M):
            if promising(T,idx,graph[row]) == 255:
                _not_visited.append((row,idx))
                temp.append(255)
            else:
                temp.append(0)
        comp_graph.append(temp)
    
    return comp_graph

def DFS(x,y):
    global cnt
    # 상하좌우에 255 없으면 종료
    # 상하좌우에 255 있으면 재귀
    # 255 방문 다 끝나면 (255 방문했는지 체크)
    if len(_not_visited) == 0:
        return cnt


    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<N and 0<=ny<M:
            if graph[nx][ny] == 255 and ((nx,ny) in _not_visited):
                cnt -=1
                _not_visited.remove( tuple( (nx,ny) ) )
                DFS(nx,ny)

    cnt+=1

    # 255 방문 다 끝나면 (255 방문했는지 체크)
    if len(_not_visited) == 0:
        return cnt

    X,Y = _not_visited.pop(0)
    DFS(X,Y)

if __name__ == '__main__':
    
    cnt = 0 # 255 개수
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    N, M = map(int,input().split()) # 세로 N , 가로 M

    # 초기 graph 값
    graph = []
    for _ in range(N):
        input_ = list(map(int,input().split()))
        graph.append(input_)
    
    # 구분선 입력
    T = int(input())
    T = 3*T


    # 255 좌표 기억
    _not_visited = []

    graph = _comp(graph) # 압축
    
    if len(_not_visited) == 0:
        print(cnt)
    else:
        X,Y = _not_visited.pop(0)
        cnt +=1
        DFS(X,Y)

        print(cnt)