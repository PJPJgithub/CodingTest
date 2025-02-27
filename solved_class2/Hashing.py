#https://www.acmicpc.net/problem/15829
import sys

sys.stdin=open("input.txt","r")

l = int(input())
string = input()

r = 31
m = 1234567891

ans = 0

for i in range(len(string)):
    ans += (ord(string[i])-96)*(r**i)

print(ans%m)