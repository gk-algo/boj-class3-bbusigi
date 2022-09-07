from collections import defaultdict
from itertools import combinations
from functools import reduce


if __name__ == "__main__":
    result = []
    for _ in range(int(input())):
        data = defaultdict(int)
        for _ in range(int(input())):
            info = input().split(' ')
            data[info[1]] += 1
        
        cnt = 0
        for i in range(len(data)):
            num = i+1
            c = combinations(data.values(), num)
            for tup in c:
                _val = reduce(
                    lambda acc, cur: acc * cur,
                    tup,
                    1
                )
                cnt += _val
        result.append(cnt)
    
    for i in result:
        print(i)
