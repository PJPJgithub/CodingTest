#https://school.programmers.co.kr/learn/courses/30/lessons/42895?language=python3
def solution(N, number):
    '''
    ()를 관점을 전환해서 본다 : 앞서 계산한 값을 '재사용'
    *최적화문제
    *동적 계획법을 사용할 때, 재사용 아주 중요한 개념. 중복된 계산을 피하고 이미 계산한 값을 재사용하는 것.
    *DP가 효과적인 문제는 부분 문제로 나눠서 해결 가능하고, 중복된 계산이 발생하는 문제. 문제를 잘게 나누고 그 결과를 저장해서 재사용하는 방식.
    '''
    
    dp=[set() for _ in range(9)]#set으로 중복된 값 피하고 값 찾을때 빠르게
    '''
    dp[1] : N을 1개 쓸 때
    dp[2] : N을 2개 쓸 때
    ...
    
    '''
    dp[1].add(N)#set에 값 추가할 때, add()
    
    for i in range(2,9):
        dp[i].add(int(str(N)*i))
        
        for j in range(1,i):
            for x in dp[j]:
                for y in dp[i-j]:
                    dp[i].add(x+y)
                    dp[i].add(x-y)
                    dp[i].add(x*y)
                    if y!=0:
                        dp[i].add(x//y)
    
    for i in range(1,9):
        if number in dp[i]:
            return i
            
    return -1

