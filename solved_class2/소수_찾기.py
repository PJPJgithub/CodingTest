'''
문제
주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

입력
첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

출력
주어진 수들 중 소수의 개수를 출력한다.
'''
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
