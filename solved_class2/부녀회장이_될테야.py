#https://www.acmicpc.net/problem/2775
import sys
sys.stdin=open("input.txt","r")

t=int(input())
for i in range(t):
    k=int(input())
    n=int(input())

    arr=list(range(1,n+1))
    temp = []
    a=0
    while k>0:
        k-=1
        for j in range(n):
            a += arr[j]
            temp.append(a)
        arr=temp[:]
        temp.clear()
        a=0
        
    print(arr[-1])