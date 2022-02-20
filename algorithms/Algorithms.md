# List

## 리스트 정렬

```
# Bubble Sort
def BubbleSort 


```
# Counting Sort
def CountingSort(A, B, k):
  # A - 입력 리스트 사용된 숫자(1 ~ k)
  # B - 정렬된 리스트
  # C - 카운트 리스트
  C = [0] * k

  for i in range(0, len(B)):
    C[A[i]] += 1

  for i in range(1, len(C)):
    C[i] += C[i-1]

  for i in range(len(B)-1,-1, -1):
    B[C[A[i]]-1] = A[i]
    C[A[i]] -= 1


```
# 리스트 선언의 충격과 공포
arr = [[0]*3]*4
>>>>[[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
arr[0][1] = 1
>>>>[[0,1,0],[0,1,0],[0,1,0],[0,1,0]]
arr = [[0]*3 for _ in range(4)]
>>>>[[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
arr[0][1] = 1
>>>>[[0,1,0],[0,0,0],[0,0,0],[0,0,0]]
