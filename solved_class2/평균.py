#https://www.acmicpc.net/problem/1546

import sys
sys.stdin = open("input.txt","r")

n=int(input())
arr=list(map(int,input().split()))
m = max(arr)

for i in range(n):
    arr[i] = arr[i]/m*100

print(sum(arr)/n)