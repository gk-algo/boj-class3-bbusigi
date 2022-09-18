def DFS(idx,cur_cnt):
    global cnt
    visited[idx] = 1 # 방문 처리
    #print(visited)
    if not 0 in visited: # 방문 다했으면
        if cur_cnt > cnt:
            cnt = cur_cnt
        return

    if not 1 in matrix[idx]: # 갈 수 있는 곳이 없으면
        if cur_cnt > cnt:
            cnt = cur_cnt
        return

    else:
        for col in range(1,N+1):
            #print(f'col : {col}')
            if matrix[idx][col] == 1:
                cur_cnt +=1
                #print(f'col : {col}, idx :{idx}')
                DFS(col,cur_cnt)
    

if __name__ == '__main__':    
    ## 입력 ##
    # 첫째 줄 || M개의 줄, N개의 컴퓨터
    N, M = map(int,input().split()) 
    # 둘째 줄
    matrix = [[ 0 for _ in range(N+1)] for _ in range(N+1)]
    for _ in range(M):
        A, B = map(int,input().split())
        matrix[B][A] = 1 # 단방향임

    max_cnt = 0
    max_list = []

    for k in range(1,N+1):
        ## 리스트 초기화
        visited = [0] * (N+1)
        visited[0] = 'x'    

        ## 출력
        cnt = 0
        #print(f'시작 {k}')
        DFS(k,cnt)

        if cnt > max_cnt:
            max_list.clear()
            max_cnt = cnt
            max_list.append(k)
        
        elif cnt == max_cnt:
            max_cnt = cnt
            max_list.append(k)
    
    max_list.sort()

    for i in max_list:
        print(i,end=" ")

