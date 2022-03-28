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
    현주님의 코드
   def cost(n, ssum):
      global ans
      #함수를 돌려도 값이 지속되게 했음
      
    if n > 12:
        if ans > ssum:
            ans = ssum
        return
        
    cost(n+1, ssum+arr[n] * c[0])
    cost(n+1, ssum+c[1])
    cost(n+3, ssum+c[2])
    cost(n+12, ssum+c[3])
 
 
T = int(input())
for tc in range(1, T+1):
    c= list(map(int, input().split())) # 돈 케이스를 입력받고
    arr = [0]+list(map(int, input().split())) # 달별 케이스를 입력밥는다. 
 
    ans = 9999
    cost(1, 0)
    print('#{} {}'.format(tc, ans))
    '''