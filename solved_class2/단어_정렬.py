#https://www.acmicpc.net/problem/1181
#lambda 정렬
import sys

sys.stdin=open("input.txt","r")

n=int(input())
arr = []
for i in range(n):
    arr.append(input())

arr = list(set(arr))

arr.sort(key = lambda x: (len(x),x))

for i in (arr):
    print(i)