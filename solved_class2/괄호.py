#https://www.acmicpc.net/problem/9012

import sys

sys.stdin=open("input.txt",'r')

t = int(input())

for i in range(t):
    s = input()
    arr = []
    for m in s:
        if m == '(':
            arr.append(m)
        elif m == ')':
            if len(arr) == 0:
                arr.append(m)
            elif arr[-1] == '(':
                arr.pop()
            else:
                arr.append(m)

    if len(arr) > 0:
        print("NO")
    else:
        print("YES")
        
