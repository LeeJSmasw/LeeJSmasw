import sys

sys.stdin = open('swimingpool.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    money_case = list(map(int, input().split()))
    month_case = list(map(int, input().split()))

    result_case = [0, 0, 0, 0]
    result_case[3] == money_case[3] #연간 가격

    pri_number = 0 # 계산을 위해 임시값
    cnt = 0 
    continue_count = 0
    for i in month_case: # 하루 가격
        result_case[0] += i * month_case[0]
        if i != 0: # 1달간 가격
            result_case[1] += month_case[1]
            
            # 세 달간 속 가격 어떻게 하면 좋을까나 음 
            
    for i in month_case: # 하루 가격
        result_case[0] += i * month_case[0]
        if i != 0: # 1달간 가격
            result_case[1] += month_case[1]
            cnt += 1 
            if cnt ==3:
                cnt = 0
                
                result_case[2]+= money_case[2]
                
                # case 1 :  3 3 3 3 3 3 3 문제 없음
                # case 2 :  1 하루 치 한게 쌀수도
                # case 3 :  1달 꺼한게 살 수도 
                
                
        




    result = min(result_case)

    print(f'#{tc} {result}')
    
    
    '''
    진하님 코드 오호 .. 
    T = int(input())
    for tc in range(1, 1 + T):
    d, m, m3, y = map(int, input().split())
    plan = [0]+list(map(int, input().split()))
    result = [0]*13
 
 
    for i in range(1,13):
        tmp = [0,0,y,y]
        # 1일 이용권 사용
        tmp[0] = result[i-1] + plan[i]*d
        # 1달 이용권 사용
        tmp[1] = result[i-1] + m
        # 3달 이용권 사용
        if i>=3:
            tmp[2] = result[i-3] + m3
            #이게 왜 성립할까나 
        result[i] = min(tmp)
    print(f'#{tc} {result[12]}')
    
    
    def cal(month, day):
      global result
    # print(month, day)
 
    if month > 12:
        if result > day:
            result = day
    else:
        # 하루
        cal(month + 1, day + plan[month]*fee[0])
        # 한달
        cal(month + 1, day + fee[1])
        #세달
        cal(month + 3, day + fee[2])
 
    if result > fee[3]:
        result = fee[3]
    return
 
T = int(input())
 
for tc in range(1, T+1):
    fee = list(map(int, input().split()))
    plan = [0] + list(map(int, input().split()))
    result = 99999999999
 
    cal(0, 0)
    print(f"#{tc} {result}")
    
    '''