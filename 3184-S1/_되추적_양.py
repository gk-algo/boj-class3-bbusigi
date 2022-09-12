# .(점) = 빈 필드 // # = 울타리 // o = 양 // v = 늑대 
# 수평/수직으로만 이동 

def promising():
    pass

def DFS(x,y):
    global w,s
    visited[x][y] = 1

    temp_list.append([x,y])
    # 상하좌우 정의


    # 늑대, 양 있는 필드 공간 검색 다 확인시

    while temp_list:
        x,y = temp_list[0][0],temp_list[0][1]
        del temp_list[0]

        if farm_field[x][y] == 'v':
            w +=1
        elif farm_field[x][y] == 'o':
            s+=1


        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < R and 0 <= ny < C:
                # 좌로 이동
                if farm_field[nx][nx] != '#' and visited[nx][ny] == 0:
                    # 늑대 발견시, 늑대 수 증가, 리스트에서 삭제
                    temp_list.appned([nx,ny])
                    visited[nx][ny] = 1




if __name__ == '__main__':
    temp_list = []
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    R , C = map(int,input().split()) # 3<= R , C<=250 행 / 열 의 수
    sheep = 0 ; wolf = 0
    visited = [[0] * C for i in range(R)]
    farm_field = [list(input()) for _ in range(C)]
    for x in range(R):
        for y in range(C):
            if farm_field[x][y] == 'o':
                sheep +=1
            elif farm_field[x][y] == 'v':
                wolf += 1

    for x in range(R):
        for y in range(C):            
            if (farm_field[x][y] == 'o' or farm_field[x][y] == 'v') and visited[x][y] == 0:
                w = 0
                s = 0
                DFS(x,y)

                if w>=s:
                    s = 0
                else:
                    w = 0
                
                wolf += w
                sheep += s
