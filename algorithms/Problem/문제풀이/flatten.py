import sys
sys.stdin = open("flatten_input.txt", "r")

for tc in range(1, 11):
    number = int(input())
    data_list = list(map(int, input().split()))
    max = 0
    min = data_list[0]
    max_index = min_index = 0
    count = 0
    while count <= number:
        for i in range(len(data_list)):
            if max < data_list[i]:
                max = data_list[i]
                max_index = i

            elif data_list[i] < min:
                min = data_list[i]
                min_index = i

        data_list[max_index] -= 1
        data_list[min_index] += 1
        max -= 1
        min += 1
        count += 1

    print(f'#{tc} {max - min+2}')

#
# for tc in range(1, 11):
#     dump_count = int(input())
#     boxs_list = list(map(int, input().split()))
#
#     # 최대값과 최솟값이 있는 인덱스를 0으로 초기화.
#     min_idx, max_idx = 0, 0
#
#     # dump_count가 1일 때 마지막으로 while문 돌아야 함.
#     while dump_count > 0:
#         # 최대값과 최소값이 있는 인덱스 찾기. 가로 길이는 항상 100으로 주어진다
#         for i in range(100):
#             if boxs_list[i] < boxs_list[min_idx]:
#                 min_idx = i
#             if boxs_list[i] > boxs_list[max_idx]:
#                 max_idx = i
#
#         if boxs_list[max_idx] == boxs_list[min_idx]:
#             print(f'#{tc} {boxs_list[max_idx] - boxs_list[min_idx]}')
#             break
#         if boxs_list[max_idx] != boxs_list[min_idx]:
#             # max값에서 1 빼고 min 값에 1 더하기. dump_count 1감소.
#             boxs_list[max_idx] -= 1
#             boxs_list[min_idx] += 1
#             dump_count -= 1
#
#         # max와 min이 같다면 0을 프린트하고 while문을 끝낸다
#         for i in range(100):
#             if boxs_list[i] < boxs_list[min_idx]:
#                 min_idx = i
#             if boxs_list[i] > boxs_list[max_idx]:
#                 max_idx = i
#
#     print(f'#{tc} {boxs_list[max_idx] - boxs_list[min_idx]}')