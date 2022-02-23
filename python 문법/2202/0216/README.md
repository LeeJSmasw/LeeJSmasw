# 문자열 알고리즘



글이 있을 때 특정한 문자를 찾는 알고맂즘 (cnt +f 같은거)



## 1.  문자열 매칭 알고리즘



 단순 비교 문자열 매칭 알고리즘 (하나씩 확인하는 알고리즘 - 가장 간단한 형태의 알고리즘)

```markdown
긴 글      B | c | D | E | F
찾을 문자   D | E


긴 글      B | c | D | E | F
찾을 문자	   D | E

긴 글      B | c | D | E | F
찾을 문자		   D | E 

O(N*M)의 사간 복잡도를 가짐
```



- KMP (단순하게 모두 비교하면 시간이 너무 오래걸릴수 있음)

```
접두사 | 접미사 
a b c | a b a
문자열 최대일치 길이 // 접두사와 접미사가 같은경우 점프가 가능하다???
1 1.1 1.2 1.3~~
j ix i-->
a b a c a a b a
0 0 1 
```





-출처 : 동빈난님 강의  https://www.youtube.com/watch?v=yWWbLrV4PZ8&list=PLRx0vPvlEmdDHxCvAQS1_6XV4deOwfVrz&index=3