#https://www.acmicpc.net/problem/2869
import sys
import math
sys.stdin=open("input.txt","r")

a,b,v=map(int,input().split())

print(math.ceil((v-a)/(a-b)) + 1)