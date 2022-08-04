'''
이때 괴물이 있는 부분은 0으로, 괴물 이 없는 부분은 1로 표시
# N X M 크기 직사각형 미로 

# (1,1) 미로의 출구 (N,M)으 ㅣ 위치에 존재하며 한 칸씩 이동
1로 다녀야함, 0을로는 못감 ㅇㅋ
입력 에시
5 6 # 5* 6칸이라는거지
101010
11111111
00000001
1111111
111111

힌트 BFS... 
'''

from collections import deque

n,m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int,input())))
    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 소스코드 구현
def bfs (x, y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x, y =queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            
            if graph[nx][ny] == 0:
                continue
            
             #모르겠음... 음 