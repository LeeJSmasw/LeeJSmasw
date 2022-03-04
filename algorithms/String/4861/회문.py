import sys
sys.stdin = open('4861.txt','r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    alpha = [input() for _ in range(N)]
    half = M//2

    ans = ''
    for i in range(N):
        for j in range(N):
            # 가로줄이 회문인가?
            check = 0
            if j <= N-M:
                for k in range(half):
                    # 회문인지 검증
                    if alpha[i][j+k] == alpha[i][j+M-k-1]:
                        check += 1
                    else:
                        print('K')
                        break
                    # 회문 발견, 문제 조건중 회문은 반드시 하나만 있다.
                    # 회문을 발견한 index와 가로줄인지 여부를 저장(가로의 경우 is_row=True)
                    if check == half:
                        y, x, is_row = i, j, True
                        break

            # 세로줄이 회문인가?
            check = 0
            if i <= N-M:
                for k in range(half):
                    if alpha[i+k][j] == alpha[i+M-k-1][j]:
                        check += 1
                    else:
                        break

                    if check == half:
												# 세로줄에서 발견한 경우 is_row = False
                        y, x, is_row = i, j, False
                        break

    for i in range(M):
			  # 가로줄에서 찾았을 경우(is_row == True)  
			  # 세로줄에서 찾았을 경우(is_row == False)
        ans += alpha[y][x+i] if is_row else alpha[y+i][x]
    print(f"#{tc} {ans}")