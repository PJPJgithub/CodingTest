#https://www.acmicpc.net/problem/2739
'''
문자열 출력 부분 참고
'''
import sys
sys.stdin=open("input.txt",'r')

n=int(input())

for i in range(1,10):
  print(str(n) + ' * ' + str(i) + ' = ' + str(n*i))