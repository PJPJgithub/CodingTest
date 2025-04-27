#https://www.acmicpc.net/problem/11866
'''
deque의 rotate() : 원형을 회전시키는 함수, 즉 원하는 값을 위치를 바꿔 뺄 수 있다.
'''
import sys
from collections import deque

sys.stdin=open("input.txt",'r')

n,k=map(int,input().split())

arr=list(range(1,n+1))
q=deque(arr)
'''
q = deque(range(1, n+1))
'''
ans = []

while len(q) > 0:#while q:
  for i in range(k-1):
    q.rotate(-1)
    print(q)
  ans.append(q.popleft())

#print('<' + ', '.join(map(str, ans)) + '>')
print('<',end='')
for i in range(len(ans)):
  if i == len(ans)-1:
    print(ans[i],end='>')
  else:
    print(ans[i], end=', ')