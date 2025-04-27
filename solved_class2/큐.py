#https://www.acmicpc.net/problem/10845
'''
from collections import deque : 선언언
q=deque() : 생성
q.append() : 추가
q.appendleft() : 왼쪽에 추가
q.pop() : 제거
q.popleft() : 왼쪽 끝 제거
len(q) : 길이
q.rotate(1) : 오른쪽 회전
q.rotate(-1) : 왼쪽 회전
q=deque([1,2,3],maxlen=?) : ?길이 넘기면 자동으로 오래된 값 삭제
'''
import sys
from collections import deque

sys.stdin=open("input.txt",'r')

def push(q,x):
  q.append(x)

def pop(q):
  if empty(q) == 1:
    print(-1)
  else:
    print(q.popleft())

def size(q):
  print(len(q))

def empty(q):
  if len(q) == 0:
    return 1
  else:
    return 0

def front(q):
  if empty(q) == 1:
    print(-1)
  else:
    print(q[0])

def back(q):
  if empty(q) == 1:
    print(-1)
  else:
    print(q[-1])

N = int(input())
q = deque()
order = []

for i in range(N):
  order.append(list(input().split()))

for i in range(N):
  if order[i][0] == 'push':
    push(q,int(order[i][1]))
  elif order[i][0] == 'pop':
    pop(q)
  elif order[i][0] == 'size':
    size(q)
  elif order[i][0] == 'empty':
    print(empty(q))
  elif order[i][0] == 'front':
    front(q)
  elif order[i][0] == 'back':
    back(q)
  else:
    print('error')