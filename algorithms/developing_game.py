#첫쨰 줄에 맴의 세로크기 N과 가로 크기 M을 공백으로 구분하여 입력한다. (3<=)
'''
 -0 : 육지
 -1 : 바다 
 입력 예시
 4 4 # 4x4
 1 1 0
 1 1 1 1
 1 0 0 1
 1 1 0 1
 1 1 1 1
'''
from filecmp import dircmp


n, m = map(int, input().split()) # 왜 노란줄을 보이는거야 친구

d = [[0]*m for _ in range(n)] #이게 정말 개쩐다

x, y, direction = map(int, input().split())
d[x][y] = 1 # 현재 위치를 잡는거야?? 개쩐다

array = []
for i in range(n):
    array.append(list(map(int, input().split())))
    
    
dx = [-1,0,1,0] # 북 동 남 서  # 통상적인 x좌표가 아닌가
dy = [0,1,0,-1]# 북 동 남 서 이게 왜 x랑 y좌푤르 이렇게 잡는가 생각을 해봐야

# 행렬이라고 생각했을떄 행(x) 열 (y)로 잡아서 그런가..?

def turn_left()
