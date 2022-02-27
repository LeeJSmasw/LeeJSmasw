import sys
sys.stdin = open('6458_input.txt','r')

T = int(input())
for tc in range(1,T+1):
    N = int(input()) # 입력 되는 케이스
    bus_stop = [0] * 5001 # 1부터 5000까지 있으니까 0은 걍 있다고치고 1부터 5000까지 선언하기 위해 1을 더함 ㅎ
    real_bus = [] # cj 정보를 받을 리스트임
    result = '' #결과를 받을 리스트임
    
    for _ in range(N):
        ai, bi = map(int,input().split())
        for i in (ai, bi+1):
            bus_stop[i] += 1
        

    P = int(input())
    
    

    for c in range(P): # cj 정보를 받아보자
        bus_use = int(input())
        real_bus.append(bus_use)

            
    for k in real_bus:
        
            result += str(bus_stop[k]) + ' '


    print(f'#{tc} {result}')
    
    
#천소희님의 코드
tc = int(input())
 
for t in range(1, tc + 1):
    N = int(input())
    bus_cnt = [0] * 5000
 
    for i in range(N):
        start, end = map(int, input().split())
        for j in range(start - 1, end):
            bus_cnt[j] += 1
 
    P = int(input())
 
    result = ''
 
    for i in range(P):
        result += str((bus_cnt[int(input())-1])) + ' '
 
    print(f'#{t} {result}')