#https://www.acmicpc.net/problem/4153
import sys

sys.stdin = open("input.txt","r")

while True:
    ans = list(map(int, input().split()))
    if ans[0] == 0 and ans[1] == 0 and ans[2] == 0:
        break
    ans.sort()
    if ans[2]**2 == (ans[0]**2) + (ans[1]**2):
        print("right")
    else:
        print("wrong")
