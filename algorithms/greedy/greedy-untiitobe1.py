# 1이 될떄 까지
#입력 조건
'''
첫째 줄에서 N(2<=2<=100,000)과 K(2<=k<=100,000)가 공백으로 구분됨 각각
자연수로 주어진다. 이때 입력으로 주어지는 N은 항상 K보다 크거나 같다.
'''
#출력 조건
'''
첫째 줄에 N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 횟수의 최솟값을 출력한다.
'''
# 입력 예시 25 5 출력 예시 2
N,k = map(int,input().split(' '))
cnt =0
# def first(a,b):
#     a = a//b
#     return a

# def second(a):
#     a = a-1
#     return a

while N!=1: #1이 되면 멈추니까 조건에서 N은 항상 K보다 크거나 같으니까 문제 없겠지
    if N%k ==0:
        N = N//k 
        # print(first(N,k))
        cnt +=1
        # print(cnt)
    else:
        N = N-1
        cnt +=1
        # print(cnt)
print(cnt)