#https://www.acmicpc.net/problem/10816

'''
Counter 사용법

from collections import Counter : 딕셔너리 형태로 리스트의 각 원소가 몇개 있는지 알려준다.

count = Counter(?)
count[1] : key값이 1인 value
'''

import sys
from collections import Counter

sys.stdin=open("input.txt",'r')

n = int(input())
sang = list(map(int,input().split()))

m = int(input())
arr = list(map(int,input().split()))

sang_cnt = Counter(sang)

for i in arr:
  print(sang_cnt[i], end=' ')