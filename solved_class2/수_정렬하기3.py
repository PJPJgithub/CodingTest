import sys

input = sys.stdin.readline
N = int(input())  # 수의 개수
count = [0] * 10001  # 1 ~ 10000 까지 저장

for _ in range(N):
    num = int(input())
    count[num] += 1

output = sys.stdout.write
for i in range(1, 10001):
    if count[i] > 0:
        output((str(i) + '\n') * count[i])
