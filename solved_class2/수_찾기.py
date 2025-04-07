#https://www.acmicpc.net/problem/1920
'''
data의 크기가 클 때, 집합으로 변환하면 빠른 조회가 가능하다.
list : O(N) , set : O(1)
'''

import sys

sys.stdin = open("input.txt", "r")

n = int(input())
nrr = list(input().split())
m = int(input())
mrr = list(input().split())

def check_existence(N, A, M, X):
    # 리스트 A를 집합으로 변환하여 빠른 조회 가능하게 함
    A_set = set(A)
    
    # 각 X의 요소가 A 집합에 존재하는지 확인
    result = []
    for x in X:
        if x in A_set:
            result.append(1)
        else:
            result.append(0)
    
    return result

result = check_existence(n,nrr,m,mrr)

for res in result:
    print(res)