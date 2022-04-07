#시작 노드부터 우선적으로 가까운 노드로 우선적으로 탐색하는 알고리즘
# 큐 자료구조
# Breath First Search 
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    print(queue)
    
    while queue:
        v = queue.popleft()
        print(v, end='')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
#난 이노드 만드는게 더 신기하다.. 맨밑에서부터 시작이나        
graph = [
    [],
    [2,3,8],
    [1,7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2,6, 8],
    [1,7]
]

visited = [False] *9

bfs(graph, 1, visited)

'''
 q는 먼저 들어온걸 찾아준다
 1
 2   3 
 4 5  6 7 
 1 -> 2->3 -> 4->5 -> 6->7
 1234567
    '''