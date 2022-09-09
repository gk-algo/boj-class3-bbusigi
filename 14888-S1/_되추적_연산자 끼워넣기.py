import sys
input = sys.stdin.readline

def cal_sort(cnt,number):
    global add,minus,multiple,divide,MAX_val,MIN_val

    if cnt == N:
        MAX_val = max(MAX_val,number)
        MIN_val = min(MIN_val,number)

    else:

        if add > 0:
            add -=1
            cal_sort(cnt+1,number + _NUM[cnt])
            add +=1
        if minus > 0:
            minus -=1
            cal_sort(cnt+1,number - _NUM[cnt])
            minus +=1
        if multiple > 0:
            multiple -=1
            cal_sort(cnt+1,number * _NUM[cnt])
            multiple +=1
        if divide > 0:
            divide -=1
            cal_sort(cnt+1,int(number / _NUM[cnt]))
            divide +=1


if __name__ == '__main__':
    N = int(input()) # 수의 개수 (2<=N<=11)
    _NUM = list(map(int,input().split())) # 수열
    add, minus, multiple , divide = map(int,input().split()) # 연산자 개수 (+ - x %) 순서

    MAX_val = -sys.maxsize
    MIN_val = sys.maxsize

    cal_sort(1,_NUM[0])

    print(MAX_val)
    print(MIN_val)
