#https://www.acmicpc.net/problem/2751
#한번에 입력 받는 값이 클 때, sys.stdin.read 이용
#sorted()가 젤 빠른 정렬 알고리즘
import sys
#sys.stdin=open("input.txt","r")
input = sys.stdin.read

data = input().split()

n=int(data[0])

numbers = list(map(int,data[1:]))

sorted_numbers=sorted(numbers)

for i in sorted_numbers:
    print(i)