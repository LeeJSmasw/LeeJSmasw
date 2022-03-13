# OS

운영체재(os) 에서 제공하는 기능을 구현하는 함수들이 탑재된 라이브러리임 

1. os.getcwd() : 폴더의 현재 위치 찾기
2. os.chdir() : 폴더 이동하기
3. 파일 객체 = open('파일 이름', 파일 열기 모드) : 객체 이름 안열어도 열리긴 하지만, open.write('~~~') f.write('~')  요런 바이브임 그러므로 객체 이름을 써줘서 간단하게 사용
4. seek() : 커서 위치 이동 `0` 문서 처음으로 이동하기 



### with문

파일을 두개열 때 문제가 발생할 수 있음 ( 브라우저를 닫지 않고 다시 오픈할 경우)

```markdown
f = open('abcd.txt', 'w')
f.write('I Went to School today')

f = open('text.txt', 'w')  <- 요래 버리면 오류가 발생함
그러므로

with open('text.txt','w') as f:
	f.write('나는 오늘 학교갔었다')
```



# re

re : 정규표현식 모듈, 긴 문자열에서 특정 규칙을 가진 문자열을 찾거나, 어떤 패턴을 가진 문구를 찾는데 유용합니다. 

 1. re.match(패턴, 문자열)

    ```markdown
    pattern = r'life' 패턴을 객체에 저장합니다. , 패턴앞에는 r을 써주는게 포인트임
    script = 'life'
    re.match(pattern, script ) # 스크립트에서 패턴을 찾아보자잉
    re. match(pattern, script).group() # group() 매서드를 사용해 매치된 내용을 반환합니다.
    
    def refinder(pattern, script):
    	if re.match(pattern,script)
    		print('Match!')
    	print('Not a match')
    
    
    # 한계점 
    대소문자 구분 ㄴㄴ
    중간에 있는걸 못찾음  --> 대신 search 메소드는 찾을 수 있음
    
    pattern = r'is'
    script = 'Life is so cool'
    refinder(pattern, script)
    Not a match!
    
    
    ```

2. 

```


\d : [0-9]
\D : 숫자가 아닌 것과 매치[^0-9]
\s : whitespace 문자와 매치, [\t\n\r\f\v]와 같습니다. 맨 앞의 빈칸은 공백(space)를 의미합니다.
\S : 문자가 아닌것 과 매치
\w : 문자 +숫자와 매치, [a-zA-Z0-9]
\W : 문자+슷자가 아닌것과 매치
\\ : 메타 문자가 아닌 일반 문자 역슬래시 미치
```



# matplotlib

plt.plot(그래프 자료, 모양 + 색)
