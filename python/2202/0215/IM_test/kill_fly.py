import sys
sys.stdin = open('kill_fly.txt', "r")

T = int(input())

for tc in range(1, T + 1):
    # N: 필드 , M: MxM 크기의 파리채 쵀대한 많이 죽는 경우
    N, M = map(int, input().split())
    fly_data = [list(map(int, input().split())) for _ in range(N)]
    # 조건 5 <= N <= 15, 2 <= 2 <= M, 최대 파리 수는 30이하이다잉
    max_value = 0


    # 바꿔주는 기능
    for _ in range((N - M) +1):
        sum = 0
        # i가 0 일때 0 1 0 0 1 1 두개
        for j in range(M):
            for k in range(M):
                sum += fly_data[j + _][k + _]
        if max_value < sum:
            max_value = sum

    print(f'#{tc} {max_value}')

    # for square in range(N_M[0]):
    #     fly_count = list(map(int, input().split()))
    #     N_square.append(fly_count)
    #
    # dead_fly = 0
    # max_fly = 0
    #
    #
    # # 전체 박스를 한번씩 훑어본다.
    # for width in range(N_M[0] - N_M[1] + 1):
    #     for height in range(N_M[0] - N_M[1] + 1):
    #         for h in range(height, height + N_M[1]):
    #             dead_fly += sum(N_square[h][width:width + N_M[1]])
    #
    #             # 죽은 파리의 갯수가 최대값보다 크면 교체하고 죽은파리 리셋
    #         if max_fly < dead_fly:
    #             max_fly = dead_fly
    #             dead_fly = 0
    #         else:
    #             dead_fly = 0
    # print(f'#{t + 1} {max_fly`}')