#https://www.acmicpc.net/problem/2231
#import sys

#sys.stdin = open("input.txt", 'r')

def find_smallest_constructor(N):
    # 가능한 모든 생성자를 반복합니다
    for i in range(1, N):
        # i의 각 자리 숫자의 합을 계산합니다
        digit_sum = sum(int(digit) for digit in str(i))
        # 분해합을 계산합니다
        decomposition_sum = i + digit_sum
        # 분해합이 N과 같은지 확인합니다
        if decomposition_sum == N:
            return i
    return 0

# 입력값을 받습니다
N = int(input())

# 가장 작은 생성자를 찾습니다
smallest_constructor = find_smallest_constructor(N)

# 결과를 출력합니다
print(smallest_constructor)