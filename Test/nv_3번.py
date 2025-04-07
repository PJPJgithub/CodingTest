'''
1차원 배열 fruit안의 원소를 k개 뽑는 조합의 경우를 모두 찾고 그 경우의 값을 섞는다. 섞는다는 것은 fruit 안의 원소가 "1110"와 "0001"일 때, "1111"이 되는 것을 의미한다. 1차원 배열 fruit와 k가 주어질 때, 중복을 제외한 경우의 수를 리턴하는 result를 구하시오.
*2<=len(fruit)=n<=100
*2<=len(fruit[i])=m<=12
*1<=k<=n

[input]
fruit:["1100","0110","0011","1100"], k:2

[output]
result:4
'''
'''
combinations()는 튜플로 값 리턴 ex) combo = ("1100","0100")
zip(*combo)를 사용하면 문자열을 세로 기준으로 묶어줌 ex) list(zip(*combo)) : [('1','0'),('1','1'),...]
any(bit == '1' for bit in chars) : chars안에 '1'이 하나라도 있으면 True, 아니면 False
''.join(...) : 하나의 문자열로 합침침
'''
from itertools import combinations

def count_unique_combinations(fruit, k):
    unique_results = set()
    
    for combo in combinations(fruit, k):  # k개의 조합 생성
        mixed = ''.join('1' if any(bit == '1' for bit in chars) else '0' for chars in zip(*combo))
        unique_results.add(mixed)  # 중복 제거
    return len(unique_results)

# 테스트 예제

fruit = ["1100", "0110", "0011", "1100"]
k = 2

#fruit = ["100","100","011","100","111","011"]
#k = 1

#fruit = ["100","100","011","100","111","011"]
#k = 5

#fruit = ["001","001","001","010","010","010","100","100","100"]
#k = 3
print(count_unique_combinations(fruit, k))