import sys
sys.stdin = open('Othello.txt','r')

T = int(input())

print(f'{T} {}')

'''
종훈님의 코드 // 분석해 보자 
def over(a, b): 
    if 0 <= a <= N and 0 <= b <= N:
        return True
    return False # a와 b가 모두 N, M 보다 클 때 게임이 끝남 // 와 이걸 놓쳤었네 >>  한 변 길이 N과 플레이어가 돌을 놓는 횟수 M이 주어진다. N은 4, 6, 8 중 하나이다.
 
 
T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split()) # 여기서 N과 M을 입력 받곱 
    bode = [[0] * (N + 1) for _ in range(N + 1)]
    start = N // 2
    bode[start][start] = bode[start + 1][start + 1] = 2
    bode[start + 1][start] = bode[start][start + 1] = 1
    for m in range(M):
        x, y, st = map(int, input().split())
        bode[y][x] = st
        for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)):
            revers = []
            for k in range(1, N):
                new_y = y + dy * k
                new_x = x + dx * k
                if over(new_y, new_x):
                    if bode[new_y][new_x] == 0:
                        break
                    elif bode[new_y][new_x] == st:
                        for ry, rx in revers:
                            bode[ry][rx] = st
                        break
                    else:
                        revers.append((new_y, new_x))
                else:
                    break
    wst = 0
    bst = 0
    for bd in bode:
        wst += bd.count(2)
        bst += bd.count(1)
    print(f'#{t} {bst} {wst}')
    
    
 [입력]

첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 보드의 한 변의 길이 N과 플레이어가 돌을 놓는 횟수 M이 주어진다. N은 4, 6, 8 중 하나이다.

그 다음 M줄에는 돌을 놓을 위치와 돌의 색이 주어진다.

돌의 색이 1이면 흑돌, 2이면 백돌이다.

만약 3 2 1이 입력된다면 (3, 2) 위치에 흑돌을 놓는 것을 의미한다.

돌을 놓을 수 없는 곳은 입력으로 주어지지 않는다.



 [출력]

각 테스트 케이스마다 게임이 끝난 후 보드 위의 흑돌, 백돌의 개수를 출력한다.

흑돌이 30개, 백돌이 34인 경우 30 34를 출력한다.


'''