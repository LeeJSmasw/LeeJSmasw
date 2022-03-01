import sys

sys.stdin = open('change_box.txt','r')

T = int(input())

for tc in range(1, T+1):
    N, Q = map(int, input().split())
    box_data = [0] * N
    cnt = 0
    for _ in range(Q):
        L, R  = map(int, input().split())
        cnt += 1
        for i in range(L-1,R):
            box_data[i] = cnt

    result = ''
    for j in box_data:
        result += str(j) + ' '
            
            
    print (f'#{tc} {result}')
        