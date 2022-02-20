1월 정리

(싸피-1주차)지금까지 흩날려 있던 정보를 정리해보자!!! 

# 1. 스코핑
![갓토니에게 여쭤보자](README.assets/갓토니에게 여쭤보자.jpg)

하지만 이게 아니었음 .. LEGB(local -> Enclosed->global -> buit in)순이기 때문에

def test1()위로 가는게 아니라 로컬인 test2방향으로 가는거임 그래서 

a >1 #(로컬에 없으니까 글로벌에 가서 1)

b>3  #(로컬에 바로 3)

c>1  #(로컬에 로컬로가면 1)



# 2. Range



```
[a,b] # a 부터 시작 ,b미만!!, step 생략시 1
[a,b,step]
```



# 3. Enmuerate

```markdown
enumuerate(members)
=> <enumerate at 0x105ee100 #속도, 효율성
list(enumuerate(members))
=> (0, '민수'), (1, '영희'),(2,'철수') #숫자와 값의 tuple
list(enumerate(members, start=1))
=> (1, '민수'),(2, '영희'),(3, '철수') #기본값()
```





# 4 Break vs Continue vs Pass

```markdown
0 - > ㅁ x      : Break , 마주치면 끝
0 - > ㅁ -> o   : Continue, 마주치면 밑에 있는 내용
				(if ㅁ elif ㅁ, 이렇게 있으면 if 내용만 봄)
0 - > ~~ -> o   : pass
				(if ㅁ elif ㅁ, 이렇게 있으면 elif 내용도 봄;;;)


```



 # 5 컴퓨터의 실수 처리

```markdown
3.14 -3.12 == 0.12 #true 일까?? 정답은...! Nope...
3.14 -3.12 = 0.12000000001 ?????
# 이 컴퓨터의 자료구조에 의한 문제,,, 실수 구조에 대해 알게 되면 더 잘이애 하근ㅇ
```



# 6 기타: set 연산자

```markdown
| : 합집합
& : 교집합
- : 여집합
^ : 대칭자

a= {1,2,3,4}
b = {1.0, 2,3.0, 'Hello', (1,2,3)}

1. 합집합 
a|b
{(1,2,3),1,2,3,4,'hello'}

2. a &b
{1,2,3}

3. b-a
{{(1,2,3),'hello'}}

4. a^b (서로합치고 중복제거한거..ㅎ)
{(1,2,3),4,hello}
```



# 7. map,filter

```markdown
map(function, iterable)

filter(function, iterable)

list(filtert(lambda x: x%2, range(5)) # 이 결과는 2
- 필터에 사용될 함수는 트루 혹은 펄스를 반환해야 함
- 트루값은 입력해주고 펄스 값은 입구커~
def odd(*a)
	return a%2 
list(filter(odd, (1,2,3))) # 1과 3만 리스트에 들어감 오케
```



# 8. Dictonary

```markdown
a = {'이종수':기계, '종수':코딩}

a.get('이종수') > 기계
a['이종수'] > 기ㅖ

a.get('갓종수') -> None
a['갓종수'] -> 오류  
```



# 9. 위치의 박살남

```markdown
def add(x,y):
	return x+y
	
print(add(a=1, 2)) <- 앞에서 키워드로 지정하면 위치가 박살나서 오류가 뜸
```

참고자료

![image-20220122221048719](README.assets/image-20220122221048719.png)

![오 이런방법이](README.assets/오 이런방법이.PNG)

위 사진에 대 해 자세하게 풀이하자면, 가변형 변수 뒤에, a를 받을려고 할때 (1,2,3,4,5)이렇게 튜플로 입력하지 않아도

a=100으로 함

# 10. 깃

```markdown
1. 깃 이그노어 (.gitignore) 
#올려야 하지 말아야 팔이을 정리하느 거임 근데 이미 푸쉬된 파일은 깃 이그노어에 올린다고 없어지지 않음 오히려 깃 이그노어에 하고 삭제하면.. 추적이 안됨
#디렉토리 이그노어 하고 싶을떄
`디렉토리명/`
`.디렉토리` 하면 됨!

파일을 하고 싶을떈 파일 명 
예를들어 README.md를 하고 싶으면 걍
`파일명.확장자`
`README.md` 


2. 깃 원격 저장소
git remote(원격저장소에) add(더할꺼임) origin(별명) 원격저장소(http 주소)
```



# 11 . 파이썬 pip 리스트 뽑아내기

```
pip freeze > requirments.txt #requirments.txt로 피프 리스트 뽑아냄
pip install -r requirements.txt #이건 txt파일에 있는 피프 리스트들 뽑아놓는거임
```



# 12. 논리 연산자

```markdown
a = 1 and 4
print(a)
-> 4 #이는 and 결과를 내기 위해서는 뒤에 것도 확인해야 하기 때문

b = 1 or 4
print(b)
5

c = 0 and 5
print(c)
0 # 애는 걍 앞에만 봐도 0

d = 5 or 0
print(d)
-> 5
```



# 13. 마이너스 0???

```markdown
-0이 존재함 이건 데이터 구조상 부호를 맨앞에 있는 데이터(부수)로 부호를 나타내기 때문임
그러므로 -0을 처리해 줘야 하는데
이때 -0 은 0<-0.0 이거로 통과가 안됨... 그러므로 **0 제곱을 활용함
다행히 0==-0.0 은 성립함!!
```



# 14.  개꿀팁

```
반복문은 시퀀스면 가능한건 다 알지?
그럼 시퀀스인게 뭐가 있을까
1. range
2. list
3. str/?!!! 이게 중요
4. dictionary 
 그렇다면 반복할떄
 a = '0123456789' 가능?? 넵 가능
 if k in a:
 	print(k)
 0
 1
 2
 3
 4
 5
 6
 7
 8
 9 오호
```

# 15. *언팩~~ 두개는** 딕셔너리!

```
def my_func2(*a):
1	print(a)
2	print(type(a))
3	print(*a)
my_func2(1,2,3,4,5,6)
(1,2,3,4,5,6) # 함수에 넣을때 *에 의해 패킹(튜플로 변환) 되어서 출력이 튜플
그래서 타입도 튜플~
1 2 3 4 5 6 # 결과가 언팩되서 이렇게 나옴 오홈
```



# 16. 마 이게 크롤링이다

```markdown
import requests
from bs4 import BeautifulSoup

url = 'hwwtp://finance.naver.com/sise/
response = requesets.get(url).txt 오호
data = BeautifulSoup(response, 'html.parser')
kospi = data.select_one('#KOSPI_now') #이건 신뢰성 검사?? 거기서 뭐 뽑아왔던 것 같다 더 연구가 필요

result = kospi.text 
```



# 17. if문으로 변수 선언!~

```markdown
value = num if num>=0 else -num 
이렇게 연산자를 선언할때는 반드시!!!! else도 선언해야함
```



# 18. 자료 변환 이런것도 가능하구나



```markdown
def movie_info(movie):
	title = movie.get('title')
	result = {
	'제목' : title
	}
	return result
```



# 19. 함수의 수명

![image-20220122225106684](README.assets/image-20220122225106684.png)



# 20.  객체 지향 (여전히 어려움)

```markdown
Class Tier
	def__init__(self,size) # 클래스 생성 메직 메소드
	self.__t_size = size
	print("{}인치 타이어 탑재.format(self.__t_size)")
	
	@property
	def t_size(self):
	return self.__t_size
	
	@t_size.setter
	def t_size(self,size):
		if 14<= size <= 18: #파이써닉한 구간 선언이죠 ㅎㅎ
			self.__t_size = size
		else:
        	print('14~18인치 사이의 값만 지정')
        	
       
   wheel = Tier(15)
   print(wheel.t_size)
   wheel.t_size =17
   wheel.t_size =20
   print(wheel.t_size)
   
   #프로펄티 로 선언하는 이유는 이제 밖에서 함수 선언한 wheel의 t.__size에 접근해 수정해 주기 위해서임 
   ##단 사이즈를 조정해주기 위해선 t_size.setter까지 선언해줘야함!!!
   t_size에 대해서 
		
```



# 21 객체 지향 상속

```markdown
class OptionSilver(OptionBronze):
	def __init__(self):
		self.airbag()
		self.aircon() #애가 에어콘 함수를 부루는구나
		self.heat_wire() #에가 heat_wire 를 qnfmsmsrnsk

	def aircon(self):
		print("자동 에어컨")

	def heat_wire(self):
		print("핸들+앞좌석 열선시트")
		
Class OptinonGold(OptionSiver):
	def __init__(self):
		self.airbag()
		self.aircon()
		self.heat_wire()
		self.sunroof()
		
	def heat_wire(self):
		print("핸들+저노자석 열선시트")
		
		def sunroof(self):
		print("썬루프")
```

![이걸이렇게설명하다니 프리패스파이썬은 최고야](README.assets/이걸이렇게설명하다니.PNG)

#위 영상 출처: https://www.youtube.com/watch?v=ZXqzzK4C8Vg&t=748s

# 부록 OpenCV 이

### 변환 행렬과 변환

[M11 M12 M13]  [a]

[M21 M22 M23]  [b]

-이미지의 모든 좌표(a, b)는 다음의 좌표로 이동됩니다.

(M11*a + M12*b +M13, M21*a+M22*b+M23)

