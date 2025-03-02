#https://www.acmicpc.net/problem/11050
import sys
import math

sys.stdin=open("input.txt","r")

n,k=map(int,input().split())

print((math.factorial(n)//math.factorial(n-k))//math.factorial(k))

'''
factorial 재귀
def factorial(n):
  if n==0 or n==1:
    return 1
  return n*facotrial(n-1)
'''

'''
factorial 반복문
def factorial_iterative(n):
  result = 1
  for i in range(2,n+1):
    result *= i
  return result
'''