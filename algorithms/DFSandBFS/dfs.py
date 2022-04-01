def dfs(graph, v, visited):
    visited[v] = True
    print(v, end='')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
            
graph =[
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2, 6, 8],
    [1, 7],
]
#이렇게 방문했는지 안헀는지를 표시하기 위해 만든 visited 함수가 정말 좋은 아이디어 인듯!
visited = [False] * 9
dfs(graph,1,visited)

#음료수 먹기