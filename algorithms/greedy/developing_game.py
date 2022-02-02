#첫쨰 줄에 맴의 세로크기 N과 가로 크기 M을 공백으로 구분하여 입력한다. (3<=)
'''
 -0 : 육지
 -1 : 바다 
 입력 예시
 4 4 # 4x4
 1 1 0 # (1,1)에 북쪽(0)을 바라보고 서 있는 캐릭터
 #요 줄부터 이제 array로 들어가는거죠 
 1 1 1 1
 1 0 0 1
 1 1 0 1
 1 1 1 1
'''

#r갓동빈의 코드를 따라 치긴 했지만 아직 이해할려면 멀었다..

n, m = map(int, input().split())  # 3, 3 을 입력하자
d = [[0]*m for _ in range(n)] #이게 정말 개쩐다

x, y, direction = map(int, input().split())
d[x][y] = 1 # (1,1)을 입력하자 예제에선

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

print(array)
'''
array에 밑에 
값을 입력하자!

1 1 1 
1 0 0 
1 1 0 
'''
    
dx = [-1,0,1,0] # 북 동 남 서  # 통상적인 x좌표가 아닌가
dy = [0,1,0,-1]# 북 동 남 서 이게 왜 x랑 y좌푤르 이렇게 잡는가 생각을 해봐야

# 행렬이라고 생각했을떄 행(x) 열 (y)로 잡아서 그런가..?

#왼쪽으로 회전 
def turn_left():
    global direction  # 전반적이 코딩에 영향을 끼쳐야 하기 때문에 음
    direction -= 1 #왜 점점 작아지는 걸로 했고 왜 1로 선언했을까 그 이유는 0: 북 1: 동 : 2:남 -1: 서 이렇게 왼쪽을 돌아봤을 때 이걸 위함이었지!
    if direction ==-1: ##왜 -1일떄라는 조건을 걸었을까 모든게 미스터리다
        direction = 3

#시뮬레이션 시작
count = 0
turn_time =0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    turn_time +=1
    if d[nx][ny] == 0 and array [nx][ny] ==0: #이게 진짜 엄청 똑똑한 생각이라고 느낀게 내가 가는 필드랑, 맵에서 애초의 데이터를 수정하지 않으니 정말 좋은 수라고 생각한다.
        d[nx][ny] = 1
        x = nx #현재 케릭터 위치(x)
        y = ny #현재 케릭터 위치(y)
        count +=1
        turn_time =0
    #eles 구문을 적어주지 않으면 무슨 문제가 발생하지???
    
    else:
        turn_time+=1
    #아무것도 없을 때 다시 원래대로 돌아갈 수 있게 기능을 구현해야 하는데..음  일딴 turn_time이 4라는 애기는 360도 돌았다는 의미!
    if turn_time ==4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if array[nx][ny]==0:
            x=nx
            y=ny
            turn_time =0
        else:
            break
        turn_time =0
            
print(count)