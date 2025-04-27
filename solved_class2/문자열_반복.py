#https://www.acmicpc.net/problem/2675
'''
문자열 S의 각 문자 R번 반복
for i in range(T):
  for j in range(len(S[i])):
    print(S[i][j]*R[i],end='')
'''
import sys
sys.stdin=open("input.txt",'r')

T=int(input())
R = []
S = []

for i in range(T):
  a,b = input().split()
  R.append(int(a))
  S.append(b)

for i in range(T):
  for j in range(len(S[i])):
    print(S[i][j]*R[i],end='')
  print()