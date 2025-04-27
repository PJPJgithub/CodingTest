#https://www.acmicpc.net/problem/10951
'''
입력값을 한번에 읽어서 파싱하는 법
data = sys.stdin.read().split() : 문자열로 하나씩 리스트로 읽어옴옴
data=list(map(int,data)) : 숫자로 바꾸기
'''
import sys

data = sys.stdin.read().split()

data=list(map(int,data))

result = []

for i in range(0, len(data), 2):
  result.append([data[i],data[i+1]])

for i in range(len(result)):
  print(result[i][0]+result[i][1])