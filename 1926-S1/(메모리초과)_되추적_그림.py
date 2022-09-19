import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def DFS(row,col):
    global cnt
    global lg_pic

    for i in range(4):
        nx = row + dx[i]
        ny = col + dy[i]
        if -1 < nx <= n-1 and -1 < ny <= m-1:
            if graph[nx][ny] == 1 and (visited[nx][ny] == 0):
                visited[nx][ny] = 1
                lg_pic +=1
                cnt -=1
                DFS(nx,ny)

    cnt +=1


if __name__ == '__main__':
    cnt = 0 # 총 그림의 수
    max_lg_pic = 0 
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    #  첫째 줄 (세로 크기 : n) (가로 크기 : m) #
    n, m = map(int,input().split())
    # 두 번째 줄 n+1 줄까지
    graph = []
    for _ in range(n):
        temp  = list(map(int,input().split()))
        graph.append(temp)

    
    visited = [[0 for _ in range(m)] for _ in range(n)]
    ## 출력 ##
    # 첫째 줄 : 그림의 개수

    # 둘째 줄 : 가장 넓은 그림의 넓이

    for row in range(n):
        for col in range(m):
            if visited[row][col] == 0 and graph[row][col] == 1:
                lg_pic = 1
                visited[row][col] = 1
                DFS(row,col)
                max_lg_pic = max(max_lg_pic,lg_pic)

    # 그림이 하나도 없을 경우에는 가장 넓은 그림의 넓이는 0
    if cnt == 0 :
        print(0)
    else :
        print(cnt)
    
    print(max_lg_pic)