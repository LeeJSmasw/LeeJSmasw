

#첫째 줄에 모험가 수 N이 주어집니다. (1<=N<=100,000)
#둘쨰 줄에 각 모험가의 공포도의 값을 N 이하의 자연수로 주어지며, 각 자연수는 공백으로 구분합니다.

#여행을 떠날 수 있는 그룹 수의 최댓값을 출력합니다.

#입력 예시 5
#2 3 1 2 2 출력 2

# 데이터를 입력받았어 오케이
data1 = int(input())



#그렇다면 이제 입력받은 수들을 5로 묶어주는 함수를 해줘야 하는데 5보다 크면 안돼.. 그럼 우선 큰 걸 먼저 넣자 솔팅 해서 그리고 두 개 묶어족  그걸 뺴는거야
# 3 2 // 2 2 1 요렇게 근데 만약에 4 2 3 4 1 이렇게 입력이 됐다고 쳐봐 그러면 
# 내가 큰거 먼저 넣고 하는게 안될 수 있dj .. 
data2 = list(map(int,input().split()))
data2.sort()
print(data2)
'''
더 디테일한 정보
모헙가 길드자인 동빈이는 모험가 그룹을 안전하게 구성하고자 공포도가 X인 모험가는 반드시 X명 이상으로
구성한 모험가 그룹에 참여해야 여행을 떠날 수 있도록  규정했습니다.
ㅇㅋㅇㅋㅇㅋ 이제 이해했어

여행을 떠날 수 있는 그룹 수의 최댓ㅅ값.. 1
'''
member=0
cnt=0

for i in data2:
    if i < data1:
        member += i
        print(i)
        if member+i > data1:
            break
        else:
            cnt +=1
    else:
        break

print(cnt)
        
#나도 꽤 한 것 같은데 이거 맞을까 검증이 안되는게 아쉽네...ㅎ
    

'''
result = 0
count = 0
for i in data:
    count = 0
    
for i in data:
    count += 1
    if count >=i:
        result +=1
        count =0
print(result)

'''