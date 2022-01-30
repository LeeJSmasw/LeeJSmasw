# 스텍 큐

# 1 
    큐 : 선입 선출 자료 구조
    큐 : 입구와 모두 뚫려 있는 터널과 같은 형태로 시각화 할 수 있음?
    은행에서 대기포를 먼저 받는 느낌
     >>>>>>>>5
     >>>>>>2 5
     >>>>3 2 5
     >>>7 3 2 5
    
    >>>>>>> 1 7 3 2 #1들어와 5나가
    >>>>> 4 1 7 3 # 4들어와 2나가

```
이걸 구현하기 위해
from collections import deque

 - 리스트 자료로 큐를 구현할 수 있지만 시간복잡도가 증가하기 때문에 
 - append(리스트와 동일하게 작동) / popleft (가장 왼쪽에 있는 놈을 빼냄)

queue.reverse()

다시말하지만 deque이 더 시간 복잡도가 우수함 / pop은 시퀀스를 조절하기 때문에 더 시간복잡도가 큼!

 # 2  재귀 함수 (Recursive Function)

 def recursive_function():
    print('재귀 함수를 호출합니다)
    recursive_function()

recursive_function(i)
def recursive_function():
    if i==100:
        return
    print(i,'번째 재귀함수에서', i+1,'번째)
    recursive_function(i+1)

recursive_function(1)

ex) 펙토리얼 구현 n! = 1x2x3x4x(n-1)Xn
def factorial_iterative(n):
    result =1
    for i in range(1,n+1):
        reult *=i
    return result

def 
