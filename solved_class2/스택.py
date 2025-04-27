#https://www.acmicpc.net/problem/10828
'''
*함수에서 로컬 변수에 접근해도 로컬 변수 변경 가능
*input을 다 받고 처리해야 시간 초과 방지
'''
import sys

sys.stdin=open("input.txt",'r')

n = int(input())
order = []
stack = []

for i in range(n):
    order.append(input().split())


def push(stack, x):
    stack.append(x)

def pop(stack):
    if len(stack) == 0:
        print(-1)
    else:
        print(stack.pop())

def size(stack):
    print(len(stack))

def empty(stack):
    if len(stack) == 0:
        print(1)
    else:
        print(0)

def top(stack):
    if len(stack) == 0:
        print(-1)
    else:
        print(stack[-1])
    
for i in range(n):
    if order[i][0] == 'push':
        x = int(order[i][1])
        push(stack,x)
    elif order[i][0] == 'pop':
        pop(stack)
    elif order[i][0] == 'size':
        size(stack)
    elif order[i][0] == 'empty':
        empty(stack)
    elif order[i][0] == 'top':
        top(stack)
    else:
        print('error')