T = int(input())
for tc in range(1, T + 1):
    money_case = list(map(int, input().split()))
    

    result_case = [0, 0, money_case[3], money_case[3]] # 3번째를 0으로 두 면 최소값의 오류가 발생함
    result = [0]*13
    month = [0]+list(map(int, input().split()))
    #month_case = list(map(int, input().split()))
    #month = [0] + month_case
    for i in range (1,13):
        result_case[0] = result[i-1] + month[i]*money_case[0] # 하루
        result_case[1] = result[i-1] + month[i]*money_case[1] # 한 달
        if i>=3:
            result_case[2] = result[i-3] + money_case[2] # 3달
        result[i] = min(result_case)     
    print(f'#{tc} {result[12]}')
    
    # continue_count = 0
    # for i in month_case: # 하루 가격
    #     result_case[0] += i * month_case[0]
    #     if i != 0: # 1달간 가격
    #         result_case[1] += month_case[1]
            
    #         # 세 달간 속 가격 어떻게 하면 좋을까나 음 
            
    # for i in month_case: # 하루 가격
    #     result_case[0] += i * month_case[0]
    #     if i != 0: # 1달간 가격
    #         result_case[1] += month_case[1]
    #         cnt += 1 
    #         if cnt ==3:
    #             cnt = 0
                
    #             result_case[2]+= money_case[2]
    # 생각해 보니 카운트 이런거 할 필요가 없는게 그냥 가격이 3달한거냐 1달에 한거냐 뭔가 더 비싼지만 보면 도ㅚㅁ 오케이ㅣ
                
                
        




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
    
    
'''
    #진하님 코드.. 이제 이해했어 이거 쩐다.
    
T = int(input())
for tc in range(1, 1 + T):
    d, m, m3, y = map(int, input().split())
    plan = [0]+list(map(int, input().split()))
    result = [0]*13
 
 
    for i in range(1,13):
        tmp = [0,0,0,y]
        # 1일 이용권 사용
        tmp[0] = result[i-1] + plan[i]*d
        # 1달 이용권 사용
        tmp[1] = result[i-1] + m
        # 3달 이용권 사용
        if i>=3:
            tmp[2] = result[i-3] + m3
        result[i] = min(tmp)
    print(f'#{tc} {result[12]}')

'''