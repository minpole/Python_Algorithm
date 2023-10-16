import time
#  그리디 알고리즘
#  <문제> 거스름 돈: 문제 해결 아이디어 (최소한의 갯수)
#  가장 큰 화폐단위 부터 돈을 거슬러 주는 것

#  정당성 분석 : 큰 단위가 항상 작은 단위의 배수이므로 
#  만약에 800원을 거스른다면? 500원 1개에 100원 3개 이겠지만, 사실 400원 2개가 효율적이다.

n  = 1260
count  = 0 

#  큰 단위의 화폐부터 차례대로 확인하기
array = [500, 100, 50, 10]
#  // : 몫
#  %  : 나머지
for coin in array:
    count += n // coin # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    n %= coin

# print("동전 몇개로?  " + str(count))
# 결론: 화폐 갯수 (K=4) 만큼 시간 복잡도 O(4)


# <문제> 1이 될 때까지
#  풀이시간     : 15분 
#  시간제한     : 2초
#  메모리 제한  : 128 MB
#  첫째 줄에 N ( 1 <= N <= 100,000  )과  K (2 <= K <= 100,000)가 공백을 기준으로 하여 각각 자연수로 주어집니다.

#  출력 조건 N이 될때까지 1번 혹은 2번의 과정을 수행하는 횟수의 최솟값을 출력
#  1번 : N에서 1을 뺍니다.
#  2번 : N을  k로 나눕니다.
#  입력 예시 : 25, 5  |  출력 예시 : 2
# import math


# N = 25
# K = 3
N, K = map(int, input().split())
result = 0
while True:
    target = (N // K) * K
    result += (N - target)
    N = target
    print("N" + str(N))
    print("K" + str(K))
    # print(K)
    if N < K: 
        break 
    result += 1
    N //=  K
    print("NR: " + str(N))
    # print(N)
# print(N)
result += (N - 1)
# print(N)
print(result)
