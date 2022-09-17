def DFS(idx,cur_cnt):
    global cnt
    visited[idx] = 1 # 방문 처리

    if not 0 in visited: # 방문 다했으면
        if cur_cnt > cnt:
            cnt = cur_cnt
        return

    if not 1 in matrix[idx]: # 갈 수 있는 곳이 없으면
        if cur_cnt > cnt:
            cnt = cur_cnt
        return

    else:
        for col in range(1,M+1):
            if matrix[idx][col] == 1:
                cur_cnt +=1
                DFS(col,cur_cnt)

    return cnt

if __name__ == '__main__':    
    ## 입력 ##
    # 첫째 줄 || M개의 줄, N개의 컴퓨터
    N, M = map(int,input().split()) 
    # 둘째 줄
    matrix = [[ 0 for _ in range(N+1)] for _ in range(N+1)]
    for _ in range(M):
        A, B = map(int,input().split())
        matrix[B][A] = 1 # 단방향임

    cnt = 0
    
    visited = [0] * (N+1)
    visited[0] = 'x'    

    for k in range(1,N+1):
        ## 출력
        print(DFS(k,cnt))
        print(cnt)