# 순차 검색

## 1. 정렬되어 있지 않는 경우
  전부다 봐야한다?
    8을 검색하는 경우
    4 | 9 | 11 | 23 | 2 | 19 | 7
    4 요기| 9 | 11 | 23 | 2 | 19 | 7
    4 | 9 요기 | 11 | 23 | 2 | 19 | 7
    4 | 9 | 11 요기 | 23 | 2 | 19 | 7
    4 | 9 | 11 | 23  요기| 2 | 19 | 7
    4 | 9 | 11 | 23 | 2  요기| 19 | 7
    4 | 9 | 11 | 23 | 2  | 19 요기| 7
    4 | 9 | 11 | 23 | 2  | 19 | 7 요기
  -- 전부다 봐야함 2일 경우

  ```
  def sequentialSearch (a, n, key)
    i <- 0
    while i<n and a[i] != key: # a[i] != key and i<n  순서를 바꿔서 a[i] != eky를 먼저 하면 키값이 존재하지 않은 경우 인덱스라 에러가 날 수가 있음
      i < i+1
    if i<n : renturn i
    else: return -1
  ```
## 2. 정렬되어 있는 경우
  ### 1. 오름차순으로 정려된 상태에서 검색을 실시한다고 가정하자.
  ### 2. 자료를 순차적으로 검색하면 키 값을 비가하여, 원소의 크기 값이 검색 대상의 키 값보다 크면 찾는 원소가 없다는 것이므로 더 이상 검색하지 않고 뿅

```
# 정렬이 되어있는 경우!

def sequentialSearch2( a, n, key): <-- 근데 나 정렬되어 있으니까 순서대로 그 값을 안다고 요따구로 풀 수 있ㄷ었다는 거지?
  i <- 0
  whiel i < n and a[i] < key : # 
    i <- i+1
  if i < n and a[i] == key :
    return i
  else : 
    return -1

```

```
# 이진 검색으로 19 찾는 경우 ?? 가운데 부터

  2 | 4 | 7 | 9 | 11 | 19 | 23

  2 | 4 | 7 | 9 요기 | 11 | 19 | 23

  2 | 4 | 7 | 9 | 11 요기 | 19 | 23

  2 | 4 | 7 | 9 | 11 | 19 요기  | 23
  
```
  def binarySearch(a , N, key)
    start = 0
    end = N - 1
    while start <= end :
      middle = (start + end ) // 2 <- 이게 굉장히 엄청난 아이디어구만 
      if a[middle] == key : # 검색 성공 
        return true
      elif a[middle] > key : 
        end = middle -1
      else :
        start = middle +1 
      return false
```

# 인덱스 

  Database Look up table 
  선택 정렬???
  정렬 할려는 구간 

  선택 정렬과정과 다른점??

  >>>> 64 기준 위치 | 25 | 10 최소값 | 22 | 11 |
   

   1. 정렬 과정
   주어진 리스트에서 최소값을 찾는다

   2. 리스트의 맨 앞에 위치한 값과 교환한다.
  >>>>  10 | 25 | 64 | 22 | 11 |

   3. 미정렬 리스트에서 최소값을 찾는다.
   >>>>  10 확정 | 25 기준 위치| 64 | 22 | 11 최소값 |

   4. 바꿔줘
   >>>>  10 확정 | 11 확정 | 64 | 22 | 25 |

  버블 sorting 이랑 다른겨?? 그림으로 그려서 설명할 수 있어야함 넘 기본적인 거임


  ```
  # 구현
  def SelectionSort(a, N) :
    for i in range(N-1) :
    midIdx = i < 걍 작다고 침
    for j in range(i+1, N) :
      if a[midIdx] > a[j]:
        minIdx = j <- 작은애 발견, 최소값 주소 바꿔
      a[i], a[minIdx] = a[minIdx], a[i]
  ```

아래는 k번째로 작은 원소를 찾는 알고리즘
- 1번부터 k번째까지 작은 원소들을 찾아 배열의 앞쪽으로 이동시키고,  배열의 k번쨰를 반환하다.

- k가 비교적 작을 때 작을 떄 유용하며 O(kn)의 수행시간을 필요로 한다.
```
def select(arr ,k ) : 
  for i in range(0, k ) :
  minIndex = i
  for j in range (i+1, len(arr)):
    if arr[minIndex] > arr[j] :
      minIndex = j 
    arr[i], arr[minIndex] = arr[minIndex], arr[i]
  return arr[k-1]

