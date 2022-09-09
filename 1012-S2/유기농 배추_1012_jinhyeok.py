import sys
from typing import Any, Dict, Optional, Union, Tuple, Type, List

sys.setrecursionlimit(10 ** 4)


class Area:
    def __init__(self, m: int, n: int, default: Optional[Any]=None):
        self.default = default
        self.size = (m, n)

        self.__map: Optional[Dict[str, Type[default]]] = None
        for x in range(m):
            for y in range(n):
                if self.__map is None:
                    self.__map = {self._loc_to_str(x, y): default}
                else:
                    self.__map[self._loc_to_str(x, y)] = default
    
    def _loc_to_str(self, x: int, y: int) -> str:
        return f'{str(x)} {str(y)}'

    def _set(self, path: Union[Tuple[int, int], List[int]], value) -> None:
        if isinstance(path, Tuple) or isinstance(path, List):
            self.__map[self._loc_to_str(path[0], path[1])] = value
        else:
            raise TypeError
    
    def update(self, path: Union[Tuple[int, int], List[int]], value) -> None:
        self._set(path, value)
    
    def find(self, path: Union[Tuple[int, int], List[int]]) -> Any:
        if isinstance(path, Tuple) or isinstance(path, List):
            return self.__map[self._loc_to_str(path[0], path[1])]
        else:
            raise TypeError


class Farm(Area):
    pass


class Visited(Area):
    def save(self, path):
        self._set(path, True)
    
    def undo(self, path):
        self._set(path, False)
    
    def find(self, path) -> bool:
        return super().find(path)


def str_to_loc(_str_path: str) -> Tuple[int, int]:
    splited = list(map(int, _str_path.split(' ')))
    return (splited[0], splited[1])


def diffuse(path: Tuple[int, int], box_size: Tuple[int, int]) -> List[Tuple[int, int]]:
    result = []

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for dir in directions:
        x = path[0] + dir[0]
        y = path[1] + dir[1]
        
        if x < 0 or x > (box_size[0]-1):
            continue
        
        if y < 0 or y > (box_size[1]-1):
            continue

        result.append((x, y))
    
    return result


class Flag:
    def __init__(self):
        self.state = False


def _dfs(path: Tuple[int, int], farm: Farm, visited: Visited, flag: Flag) -> int:
    if farm.find(path) == 0:
        return
    if visited.find(path):
        return

    flag.state = True
    visited.save(path)

    for p in diffuse(path, farm.size):
        _dfs(p, farm, visited, flag)


if __name__=="__main__":
    result = []

    for _ in range(int(input())):
        M, N, K = tuple(map(int, input().split(' ')))
        farm = Farm(M, N, 0)

        locs = []
        for _ in range(K):
            locs.append(str_to_loc(input()))
        
        for loc in locs:
            farm.update(loc, 1)
        
        visited = Visited(M, N, False)
        cnt = 0
        for loc in locs:
            _flag = Flag()
            _dfs(loc, farm, visited, _flag)
            if _flag.state:
                cnt += 1
        
        result.append(cnt)

    for i in result:
        print(i)
