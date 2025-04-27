#https://www.acmicpc.net/problem/9935

'''
문자열이 폭발 문자열을 포함하고 있는가
문자열 폭발
남은 문자열 순서대로 이어 붙이기

폭발 문자열 없을 때까지 반복

있으면 남은거 출력
없으면 'FRULA'출력

*리스트나 문자열 안에 특정한 값이 있는지 확인할 때, stack사용 하나씩 더해보며 마지막 값이 특정값과 같은지 비교
''.join(리스트) => 문자열변환
arr[-?:] : 뒤에서 ?부터 끝까지 슬라이싱
'''
import sys

sys.stdin = open("input.txt",'r')

s = input()
boom = input()

stack = []

for char in s:
    stack.append(char)
    if ''.join(stack[-len(boom):]) == boom:
        del stack[-len(boom):]
    
result = ''.join(stack)

print(result) if result else print('FRULA')