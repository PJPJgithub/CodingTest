#https://www.acmicpc.net/problem/10814
#숫자를 문자로 바꿔서 정렬하면 숫자로 정렬했을 때와 다를 수 있다.
#숫자는 문자로 바꿔서 정렬하지 않기!
import sys

sys.stdin=open("input.txt","r")

n=int(input())
arr=[]

for i in range(n):
  age, name = map(str, input().split())
  age = int(age)
  arr.append((age,name))

arr.sort(key=lambda x : x[0])

for i in arr:
  print(i[0],i[1])