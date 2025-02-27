#https://www.acmicpc.net/problem/30802
import sys

sys.stdin = open("input.txt","r")

n = int(input())
shirts = list(map(int,input().split()))
t,p = map(int,input().split())
ans = 0

for i in range(len(shirts)):
    if 0 < shirts[i] <= t:
        shirts[i] = -1
        ans += 1
    else:
        ans += (shirts[i]+t-1)//t

print(ans)
print(n//p, n%p)