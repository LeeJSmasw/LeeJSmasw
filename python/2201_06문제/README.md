# 0123 파이썬 공부



## 1 메뉴 세기

```markdown
#나의 코딩
import json


def menu_count(restorant):
    how_many =len(restorant.get('menus'))
    return how_many
    

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    restorant = {
        "id": 11,
        "user_rating": 5.5,
        "name": "김밥나라",
        "menus": ["참치김밥", "치즈라면", "돈까스", "비빔밥"],
        "location": "서울특별시 강남구 역삼동 123-123"
    }
    print(menu_count(restorant)) # 4

```



```markdown
#권위자의 코딩

import json


def menu_count(restorant):
    for menu in restorant['menus']: 
    	result += 1

    # dict에서 특정 value를 확인하는 방법
    # 1. [key] -> 대괄호에 key 넣어서 확인하기
    # print(restorant['menus'])
    # 2. dict.get(key) -> get 함수 사용해서 확인하기
    # print(restorant.get('menus'))


    # 최종 제출 변수
    result = 0 
    # 메뉴스 리스트만 순회
    # restorant이 가지고 있는 'menus' 키의 값
    # 리스트들 순회...
    for menu in restorant['menus']: 
        # 개수 하나당 result += 1
        result += 1
    # 최종 제출
    return result
    # return len(restorant['menus'])

    

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    restorant = {
        "id": 11,
        "user_rating": 5.5,
        "name": "김밥나라",
        "menus": ["참치김밥", "치즈라면", "돈까스", "비빔밥"],
        "location": "서울특별시 강남구 역삼동 123-123"
    }
    print(menu_count(restorant)) # 4

```

# 2  maximim ,minimum

```markdown
#권위자의 풀이
def turn(temperatures):
    pass
    # 여기에 코드를 작성합니다.
    # 최종 제출 변수 만들기
    # 비어있는 딕셔너리... result = {}
    # 어??? {} 이거 세튼데...? 하면 혼나요
    # 세트는 {} <- 이걸로 비어있는 세트 못만들어요
    # 그럼 왜 dict() 말고 {}로 만들었느냐...? 는 조금있다가 보죠 ^^;
    # '맥시멈', '미니멈' 키와 벨류가 없다보니
    # 리스트에 값추가하려다가 keyerror 발생했다... 
    # 처음 딕셔너리 만들때부터 값 만들어주고 가자....
    result = {
        'maximum': [],
        'minimum': []
    }
    # 전체 순회
    for temp in temperatures:
        # 리스트를 순회 했는데... 또 리스트가 나왔다...
        # print(temp)
        # 또 순회... 해야할까?
        # 상황에 따라 다르다...
        # 우리가 해야 할 일
        # 두 기온중에, 높은 온도를 maximum에 집어넣고
        # 낮은 온도는 minimum에 집어 넣을 것이다...
        # 즉, 두 기온을 비교할 수만 있으면 된다...
        # temp 리스트의 0번째와 1번째를 비교한다...
        # 0번째 요소가 1번째 요소보다 크다면?
        if temp[0] >= temp[1]:
            # result가 가진 'maximum'키의 벨류에 0번째를 추가
            # 리스트에 값 추가하기?
            # 1. list.append() 함수 사용하기
            result['maximum'].append(temp[0]) # keyerror ???
            # result에 maximum 이라는 키 없어요. 지금...
            # 그럼 어떻게 하지?
            # 처음 result 만들때...... 'maximum' 이라는 키에 해당하는
            # 비어있는 리스트 만들어주자......
            # 2. list + list
            result['minimum'] += [temp[1]]
        # 반대는?
        else:
            # 위에 넣은거랑 반대로 넣기
            result['maximum'].append(temp[1])
            result['minimum'] += [temp[0]]
```

```markdown
#나의 풀이

def turn(temperatures):
    hig_tem= []
    low_tem= []
    for tem in temperatures:
        hig_tem.append(tem[0])
        low_tem.append(tem[1])
    
    return {'maximum' : hig_tem, 'minimum' : low_tem}
```



# 3 문자열 시퀀스 활용

# (사실상 이것때문에 썻음)

```markdown
def is_id_valid(user_data):
    # 1. 0~9 ? range?
    # 도전
    # if user_data['id'][-1] ..... range(10)... 무언가랑 같다면....
    # in 연산자...?
    # 그리고 비교할 아이디의 마지막 -1을 숫자로 바꾸기
    # if int(user_data['id'][-1]) in range(10):
    #     return True
    # 오.. 처음에는 맞음...
    # 문제는 마지막 글자가 숫자가 아니면 int로 형 변환 안됨......
    # 느낌표 ! 는 int로 형변환 할 수 없음....??
    
    # 그럼... 그냥 문자열이랑 비교하자
    # 아래와 같이 작성 가능
    # numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    # if user_data['id'][-1] in numbers:
    #     return True
    # else:
    #     return False
    # 답 잘 나옴...

    # 조금더 똑똑하게 해볼까?
    # in 연산자 sequence에 쓸 수 있다.
    # 문자열도 시퀀스이다.
    numbers = '0123456789'
    if user_data['id'][-1] in numbers:
        return True
    else:
##와 ㅇ이걸 진짜 레얼 꿀티빙랃.

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    user_data1 = {
        'id': 'jungssafy5',
        'password': '1q2w3e4r',
    }
    print(is_id_valid(user_data1)) 
    # True
    
    user_data2 = {
        'id': 'kimssafy!',
        'password': '1q2w3e4r',
    }
    print(is_id_valid(user_data2)) 
    # False
```

```
#나의 풀이
from numpy import right_shift

def is_id_valid(user_data):
    answer = '0123456789'
    case=[]
        
    for score in range(len(answer)):
        if user_data.get('id')[-1] == answer[score]:
            case.append(1)
        else:
            continue
    if 1 in case:
        return True
    else:
        return False




# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    user_data1 = {
        'id': 'jungssafy5',
        'password': '1q2w3e4r',
    }
    print(is_id_valid(user_data1)) 
    # True
    
    user_data2 = {
        'id': 'kimssafy!',
        'password': '1q2w3e4r',
    }
    print(is_id_valid(user_data2)) 
    # False
```

나는 리스트를 만들어서 다시 한 번 확인하는 절차를 밟았지만 고수님은 바로 확인해버림..!

    if user_data['id'][-1] in numbers:
            return True

    for score in range(len(answer)):
        if user_data.get('id')[-1] == answer[score]:
            case.append(1)

이 구문에서 차이가 남..!
