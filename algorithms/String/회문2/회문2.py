import sys
sys.stdin = open('회문2.py','r')

for tc in range(1,11):
    #가로, 세로 각각에 대해서 직선을만 판단한다
    
    
    
    print(f'#{tc} {result}')
    
# 성규님 코드    
for t in range(10):
    tc = int(input())
    arr = [list(input()) for _ in range(100)]
 
    max_cnt = 0
    for i in range(98):
        for j in range(98):
            if arr[i][j] == arr[i][j+1] and arr[i][j-1] != arr[i][j]:
                col_l = j
                col_r = j+1
                cnt = 0
                while arr[i][col_l] == arr[i][col_r]:
                    col_l -= 1
                    col_r += 1
                    cnt += 1
                    if cnt * 2 >= max_cnt:
                        max_cnt = cnt * 2
                    if col_l == -1 or col_r == 100:
                        break
            else:
                col_l = j - 1
                col_r = j + 1
                cnt = 0
                while arr[i][col_l] == arr[i][col_r]:
                    col_l -= 1
                    col_r += 1
                    cnt += 1
                    if cnt * 2 + 1 >= max_cnt:
                        max_cnt = cnt * 2 + 1
                    if col_l == -1 or col_r == 100:
                        break
 
            if arr[j][i] == arr[j+1][i] and arr[j-1][i] != arr[j][i]:
                col_l = j
                col_r = j+1
                cnt = 0
                while arr[col_l][i] == arr[col_r][i]:
                    col_l -= 1
                    col_r += 1
                    cnt += 1
                    if cnt * 2 >= max_cnt:
                        max_cnt = cnt * 2
                    if col_l == -1 or col_r == 100:
                        break
            else:
                col_l = j - 1
                col_r = j + 1
                cnt = 0
                while arr[col_l][i] == arr[col_r][i]:
                    col_l -= 1
                    col_r += 1
                    cnt += 1
                    if cnt * 2 + 1 >= max_cnt:
                        max_cnt = cnt * 2 + 1
                    if col_l == 0 or col_r == 99:
                        break
 
    print(f'#{tc} {max_cnt}')
    
#소희님꺼

# 회문인지 검사하는 함수
def search(word):
    length = len(word)
    for i in range(length):
        if word[i] != word[-1-i]:
            return False
    # 같다면 최대값을 반환한다
    else:
        if max_len > length:
            return max_len
        else:
            return length
 
for _ in range(10):
    tc = input()
 
    max_len = 1
 
    string = [input() for _ in range(100)]
 
    t_s = ''
    t_string = []
    for i in range(100):
        for j in range(100):
            t_s += string[j][i]
        t_string.append(t_s)
        t_s = ''
 
    for i in range(100):
        for j in range(100 - max_len):
            # 제일 긴 것부터 돌리면서 회문이 맞다면 최대길이 갱신하고 넘긴다
            for k in range(100, j + max_len -1 ,-1):
                if search(string[i][j:k]):
                    max_len = search(string[i][j:k])
                    break
 
                elif search(t_string[i][j:k]):
                    max_len = search(t_string[i][j:k])
                    break
 
 
    print(f'#{tc} {max_len}')