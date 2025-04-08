#https://www.acmicpc.net/problem/1018
'''
8*8자른 것 왼쪽 위가 W일때, B일때 나눠서 최소 변경해야 하는 횟수 계산
전체 보드에서 다 잘라보기

input().strip() : 한줄씩 읽어 오는데 앞 뒤 공백 제거
float('inf') : 무한대로 설정(최솟값 비교에 용이)
'''
import sys

sys.stdin=open("input.txt","r")

def count_changes(board, start_row, start_col):
    # 첫 번째 경우: 왼쪽 위가 'W'인 체스판
    changes1 = 0
    changes2 = 0
    for i in range(8):
        for j in range(8):
            expected1 = 'W' if (i + j) % 2 == 0 else 'B'  # (0,0)부터 시작해서 번갈아 색칠
            expected2 = 'B' if (i + j) % 2 == 0 else 'W'
            
            if board[start_row + i][start_col + j] != expected1:
                changes1 += 1
            if board[start_row + i][start_col + j] != expected2:
                changes2 += 1
    
    return min(changes1, changes2)

def solve():
    N, M = map(int, input().split())  # N, M 값 입력
    board = [input().strip() for _ in range(N)]  # 보드 입력
    
    min_changes = float('inf')
    
    # 8x8 부분 보드를 슬라이딩하면서 최소 칠해야 하는 칸 계산
    for i in range(N - 7):
        for j in range(M - 7):
            min_changes = min(min_changes, count_changes(board, i, j))
    
    print(min_changes)

# 실행
solve()