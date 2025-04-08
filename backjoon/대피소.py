#https://www.acmicpc.net/problem/28215

'''
1.거리 구하는 함수
2.각 대피소와의 가장 짧은 거리 중 가장 긴 값 찾기
3.그 중 가장 작은 값 찾기

<조합>
from itertools import combinations

combinations(arr,n) : arr에서 n개 뽑기

결과값 : for c in combinations(arr,n)

'''
import sys

sys.stdin=open("input.txt",'r')

from itertools import combinations

def manhattan_distance(house1, house2):
    return abs(house1[0] - house2[0]) + abs(house1[1] - house2[1])

def max_distance_to_nearest_shelter(houses, shelters):
    max_distance = 0
    for house in houses:
        min_distance = float('inf')
        for shelter in shelters:
            distance = manhattan_distance(house, shelter)
            if distance < min_distance:
                min_distance = distance
        if min_distance > max_distance:
            max_distance = min_distance
    return max_distance

def find_optimal_shelters(houses, K):
    min_max_distance = float('inf')
    for shelters in combinations(houses, K):
        max_distance = max_distance_to_nearest_shelter(houses, shelters)
        if max_distance < min_max_distance:
            min_max_distance = max_distance
    return min_max_distance

# 예시 사용법
N,K = map(int,input().split())

houses = []

for i in range(N):
    houses.append(list(map(int,input().split())))

# 최적의 대피소를 찾아 결과 출력
result = find_optimal_shelters(houses, K)
print(result)
