# Numpy 배열

*tensor : 차원을 갖는 array

np.empty() : 10개의 원소를 임의의로 만듬 

```markdown
np.empty(10)
>> array([            nan,             nan, 1.69121096e-306, 1.69120009e-306,
       7.56587584e-307, 1.37961302e-306, 1.05699242e-307, 8.01097889e-307,
       1.29061414e-306, 8.34451928e-308])
```

np.arange(start, stop, step) : python arange랑 똑같음 ㅎ



np.linsppace(start, last, num=) 

```
np.linspace(0,10,num=5)
> array([ 0. ,  2.5,  5. ,  7.5, 10. ])
np.linspace(0,10,num=5)
>array([ 0.        ,  1.11111111,  2.22222222,  3.33333333,  4.44444444,
        5.55555556,  6.66666667,  7.77777778,  8.88888889, 10.        ])
```

x = np.ones([2,2], dtype=np.int64)

|         -         | 기능                                  | 주요 파라미터                |
| :---------------: | :------------------------------------ | ---------------------------- |
|     np.sort()     | 축, 종류, 순서를 지정하여 정렬        | axis =-1, kind, order        |
|   np.argsort()    | 지정된 축으로 정렬한 인덱스 순서 반환 | a, axis =-1 , kind, order    |
|   np.lexsort()    | 키값으로 정렬                         | keys, axis=-1                |
| np.searchsorted() | 정렬된 배열에서 요소를 찾음           | a, v, side='left', sorter    |
|  np.partition()   | 부분 정렬                             | A, kth, axis=-1, kind, order |

np.random.seed(42) <- 요거 하면 랜덤해도 같은 숙자가 나옴..  개발자가 42이를 좋아해?

np.random.randint(0,10,12) <- 0~10까지 12개 생성



배열 병합 : np.vstack , np.hstack 



```
data = np.array([1,2], [3,4],[5,6])
data[0,1]
>>2
data[1:3]
array([3,4],[5,6])
```



# flatten vs ravel

 x = np.array([1,2,3,4],[5,6,7,8],[9,10,11,12])



x. flatten()

> array([1,2,3,4,5,6,7,8,9,10,11,12])

x.ravel()

>array([1,2,3,4,5,6,7,8,9,10,11,12])



a1 = x.flatten()

a1[0] = 99

> array([99,2,3,4,5,6,7,8,9,10,11,12])

a2 = x.ravel()

a2[0] = 99

> array([99,2,3,4,5,6,7,8,9,10,11,12])

단  fltten은 원본은 변화하지 않음 즉 x[0] =1 츨력됨

하지만 ravel은 원본도 변함즉 x[0] =99로 출력됨, 그러므로 ravel이 좀 더 메모리가 효율적임



# MSE RMSE MAE MAPE

참고로 넘파이는 document가 매우 잘되어있음 특히 쥬티터에서 아래와 같이 했을 때 도움말이 잘나옴.

shift + tab,  함수? (ex max? or max?? // 이건 파이썬에서 지원하는거라 pandas 혹은 tensorflowm pytorch 모두 사용가능 ) 하면 도움말이 나옴 





# 2. 넘파이 이미즈는 왜 3차원일까

img.shape

```markdown
> (768,1124,3) 
img[::0]
>1
img[::1]
>2
1과 2가 값이 다름 즉 rgb별로 값이 다름 오케이
```

