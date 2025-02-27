#https://www.acmicpc.net/problem/1978
import sys

sys.stdin = open("input.txt", "r")

n = int(input())
arr = list(map(int, input().split()))
ans = 0

def is_prime(s):
    if s <= 1:
        return False
    for i in range(2, int(s**0.5)+1):#제곱근으로만 나눠봐도 소수인지 판별 가능
        if s%i==0:
            return False
    return True

for i in arr:
    if is_prime(i):
        ans += 1

print(ans)       
