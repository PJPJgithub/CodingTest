#https://www.acmicpc.net/problem/1259

import sys

sys.stdin=open("input.txt","r")

arr = []

while True:
    arr.append(input())
    if arr[-1] == '0':
        arr.pop()
        break

for i in arr:
    if i == i[::-1]:
        print("yes")
    else:
        print("no")