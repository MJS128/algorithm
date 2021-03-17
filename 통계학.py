#산술평균 : N개의 수들의 합을 N으로 나눈 값
#중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
#최빈값 : N개의 수들 중 가장 많이 나타나는 값
#범위 : N개의 수들 중 최댓값과 최솟값의 차이
# N(1 ≤ N ≤ 500,000)
#입력되는 정수의 절댓값은 4,000을 넘지 않는다.

#산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림
# 중앙값을 출력
#최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력
#범위를 출력
# 

import sys
from collections import Counter

input =sys.stdin.readline
n = int(sys.stdin.readline())
data = [int(sys.stdin.readline()) for _ in range(n)]
data.sort()

count = Counter(data).most_common() 
if len(count) > 1 and count[0][1] == count[1][1]:
    print(count[1][0])
else:
    print(count[0][0])

print(round (sum(data) / n) ) #평균 
print(data[n // 2]) #중앙값
print((data[-1]) - data[0]) #범위 
