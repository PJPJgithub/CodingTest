#https://www.acmicpc.net/problem/2798
import sys

sys.stdin=open("input.txt","r")

n,m=map(int,input().split())

cards = list(map(int,input().split()))

aans = 0
ans = 0

for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            aans = cards[i]+cards[j]+cards[k]
            if aans == m:
                ans = m
                break
            if ans < aans < m:
                ans = aans

print(ans)