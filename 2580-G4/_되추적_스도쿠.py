
def is_promising(x,y):
    num_list = [1,2,3,4,5,6,7,8,9]

    ## 행/열 0 개수 찾기
    for col in range(9):
        if sdoku[x][col] in num_list:
            num_list.remove(sdoku[x][col])

        if sdoku[col][y] in num_list:
            num_list.remove(sdoku[col][y])
    
    x //= 3
    y //= 3
    for row in range(x*3,(x+1)*3):
        for col in range(y*3,(y+1)*3):
            if sdoku[x][y] in num_list:
                num_list.remove(sdoku[x][y])
    
    return num_list

def DFS(x):
    global ans

    if ans:
        return

    if x == len(zeros):
        for row in sdoku:
            print(row)
        ans = True
        return
    
    else :
        (x,y) = zeros[x]
        promising =is_promising(x,y)

        for num in promising:
            sdoku[x][y] = num
            DFS(x+1)
            sdoku[x][y] = 0

if __name__=='__main__':
    ans = False
    sdoku = [list(map(int,input().split())) for _ in range(9)] # 스도쿠 그래프 만들기
    
    ## 핵심 ##
    zeros = [(i, j) for i in range(9) for j in range(9) if sdoku[i][j] == 0]

    pass