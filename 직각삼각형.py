import sys

sys.stdin = open("input.txt","r")

while True:
    a, b, c = map(int, input().split())

    if a == 0 and b == 0 and c == 0:
        break