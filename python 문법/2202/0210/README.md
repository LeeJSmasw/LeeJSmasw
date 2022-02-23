# 1. 같은 기능을 하는 함수가 있는 이유

대표적인 예 `dictionary.get()` 과 `dictionary['']`는 같은 기능을 하지만 

get은 없으면 none 은 ['']은 없으면 오류가 발생함! (list discard, remove도 마찬가지)

즉 하나는 오류 하나는 노 오류가 발생함을 이용해 코딩 



- 이건 다른 경우지만 list.extend 와  list.append는 차이가 큼

  a=[]

  a.append('coffe')

  a.extend('coffe')

  print(a)

  `>` ['coffe', 'c','o','f'~~] 어떤 바이브인지 알겠지

- list.reverse()는 거꾸로 정렬하는게 아님 걍 원본의 순서를 뒤집는거임 오해 노노

# 2. 타입별 중요한 것

## A. string

### 반드시 외울것

```python
.find(x) - x의 첫 번째 위치를 반환합니다. 만일 리스트 내에 x가 없으면, -1을 반환합니다.
.index(x) - x의 첫 번째 위치를 반환합니다. 만일 x가 리스트 내에 없으면, 오류가 발생합니다.

.replace(old, new[, count]) # *

.strip([chars]) # *
특정한 문자들을 지정하면, 양쪽을 제거하거나(strip) 왼쪽을 제거하거나(lstrip), 오른쪽을 제거합니다(rstrip). chars 파라미터를 지정하지 않으면 공백을 제거합니다.

.split([chars]) # ***
문자열을 특정한 단위로 나누어 리스트로 반환합니다.

'separator'.join(iterable) # *
iterable 의 문자열들을 separator(구분자)로 이어 붙인(join()) 문자열을 반환합니다.
다른 메서드들과 달리, 구분자가 join 메서드를 제공하는 문자열입니다.
```



### 한번씩 봐주면 좋은것

```python
.isalpha() : 문자열이 (숫자가 아닌)글자로 이루어져 있는가?
.isspace() : 문자열이 공백으로 이루어져 있는가?
.isupper() : 문자열이 대문자로 이루어져 있는가?
.istitle() : 문자열이 타이틀 형식으로 이루어져 있는가?
.islower() : 문자열이 소문자로 이루어져 있는가?
    

```



### 그 외

```python
.startswith(x) : 문자열이 x로 시작하면 True를 반환하고 아니면 False를 반환합니다.
.endswith(x) : 문자열이 x로 끝나면 True를 반환하고 아니면 False를 반환합니다.
    
    
.isdecimal(): 문자열이 0~9까지의 수로 이루어져 있는가?
.isdigit(): 문자열이 숫자로 이루어져 있는가?
.isnumeric(): 문자열을 수로 볼 수 있는가?


.capitalize() : 앞글자를 대문자로 만들어 반환합니다.

.title() : 어포스트로피(')나 공백 이후를 대문자로 만들어 반환합니다.

.upper() : 모두 대문자로 만들어 반환합니다.


lower() : 모두 소문자로 만들어 반환합니다.

swapcase() : 대 <-> 소문자로 변경하여 반환합니다.                 

```



## B. List

### 반드시 외울것

```python
.append(x) # *****
리스트에 값을 추가할 수 있습니다.

a[len(a):] = [x] 와 동일합니다.

.extend(iterable)# ***
리스트에 iterable(list, range, tuple, string) 값을 붙일 수가 있습니다.

a[len(a):] = iterable 와 동일합니다.

.pop([i]) # ***
정해진 위치 i에 있는 값을 삭제하며, 그 항목을 반환합니다.
i가 지정되지 않으면 마지막 항목을 삭제하고 되돌려줍니다.

.sort() # **  내장함수 sorted ****
리스트를 정렬합니다.
내장함수 sorted() 와는 다르게 원본 list를 변형시키고, None을 리턴합니다.
파라미터로는 key와 reverse가 있습니다


```



### 한번쯤 볼것

```python
.insert(i, x) # *
정해진 위치 i에 값을 추가합니다.

.remove(x) # *
리스트에서 값이 x인 첫번째 항목을 삭제합니다.
만일 그런 항목이 없으면 ValueError가 발생합니다.

.index(x)
x 값을 찾아 해당 index 값을 반환합니다.

.count(x)
원하는 값의 개수를 반환합니다.
```



### 그외

```python
.clear()
리스트의 모든 항목을 삭제합니다.

.reverse()
리스트의 element들을 제자리에서 반대로 뒤집습니다. 정렬하는 것이 아닌 원본 순서를 뒤집고 수정합니다.
내장함수 reversed() 와는 다르게 원본 list를 변형시키고, None을 리턴합니다.
sort와 마찬가지로, 파라미터 key와 reverse가 있습니다.

```





## C. Tuple

```python
.index(x[, start[, end]])
튜플에 있는 항목 중 값이 x 와 같은 첫 번째 인덱스를 돌려줍니다.

해당하는 값이 없으면, ValueError를 발생합니다.

.count(x)
튜플에서 x 가 등장하는 횟수를 돌려줍니다.
```





## D. Set

```python
.add(elem)
element을 셋(set)에 추가합니다.

.update(*others) #*
여러 값을 추가합니다.
반드시 iterable 데이터 구조를 전달해야합니다.

.remove(elem)
elem을 셋(set)에서 삭제하고, 셋(set) 내에 elem이 존재하지 않으면 KeyError가 발생합니다.

.discard(elem)
elem을 셋(set)에서 삭제합니다.

remove와 다른 점은 elem이 셋(set) 내에 존재하지 않아도, 에러가 발생하지 않는다는 점입니다.
```



## E. dictionary

```python
.get(key[, default]) #***
key를 통해 value를 가져옵니다.
key가 존재하지 않을 경우 None을 반환합니다. KeyError가 발생하지 않습니다.

.setdefault(key[, default])
dict.get() 메서드와 비슷한 동작을 하는 메서드로, key가 딕셔너리에 있으면 value를 돌려줍니다.
get과 다른 점은 key가 딕셔너리에 없을 경우, default 값을 갖는 key 를 삽입한 후 default 를 반환한다는 점입니다. 만일 default가 주어지지 않을 경우, None 을 돌려줍니다.

.pop(key[, default]) #***
key가 딕셔너리에 있으면 제거하고 그 값을 돌려줍니다. 그렇지 않으면 default를 반환합니다.
default가 없는 상태에서 해당 key가 딕셔너리에 경우, KeyError가 발생합니다.

.update([other]) #***
other 가 제공하는 key,value 쌍으로 딕셔너리를 덮어씁니다. other 는 다른 딕셔너리나 key/value 쌍으로 되어있는 모든 iterable을 사용 가능합니다.
keyword argument로 업데이트 하는 방법
키워드 인자가 지정되면, 딕셔너리는 그 key/value 쌍으로 갱신됩니다.
```


