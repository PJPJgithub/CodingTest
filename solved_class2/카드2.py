#https://www.acmicpc.net/problem/2164
'''
*arr.pop()는 O(1)이지만, arr.pop(0)는 O(1)이 아니다.
<que쓰는 법>
from collections import deque
q = deque(?)
q.popleft()
q.append()
len(q)
'''

import sys
from collections import deque

sys.stdin=open("input.txt",'r')

'''
1.제일 위 버림
2.제일 위에 있는 카드 제일 아래로 옮김
3.카드가 한장 남을때까지
'''

n = int(input())

arr = list(range(1,n+1))
q=deque(arr)

while len(q) != 1:
  #1
  q.popleft()

  #2
  temp = q.popleft()
  q.append(temp)

print(q[0])


