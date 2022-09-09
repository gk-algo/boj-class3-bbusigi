# 조건 :
# 대각선 break : 
# 가로/세로

def promising(N):
    for x in range(N):
        if arr[x] == arr[N] or abs(arr[x] - arr[N]) == abs(x-N):
            return False
    
    return True

def N_Queen(x):
    global answer
    if x == N:
        answer += 1
        return
    
    else:
        for i in range(N):
            arr[x] = i
            if promising(x):
                N_Queen(x+1)

if __name__ == "__main__":
    answer =0 # 결과 
    while True:
        N = int(input('N Queens 문제입니다. N을 입력하세요 :'))
        if 1<= N < 15:
            break
    
    #N = [[0 for _ in range(N)] for _ in range(N)]
    arr = [0 for _ in range(N)]
    N_Queen(0)
    print(answer)
