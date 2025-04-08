'''
이 프로그램은 n개의 저장 공간을 관리하며, 사용자(id)가 들어오고 나가는 순서를 정리하는 기능을 합니다.
각 사용자는 특정 시간이 지나면 자리비움 상태가 되거나 삭제됩니다.

a 시간이 지나면 자리비움 상태가 됨.

b 시간이 지나면 삭제됨.

저장 공간이 가득 차 있을 경우, 가장 오래 자리비움 상태인 유저를 제거하고 새로운 유저를 넣음.

만약 자리비움 상태인 유저가 없다면 -1을 반환.

*1<=n<=2000
*1<=a<b<=200,000
*3<=len(request)<=200,000 / request의 각 유저는 [time,id]형태로 주어진다.
*1<=time<=10,000,000
*1<=id<=200,000

[input]
n : 5, a : 100, b : 200, request : [[11,1],[12,2],[13,1],[16,3],[200,1],[214,1],[216,1]]

[output]
result : [1,2,2,3,3,2,1]
'''
'''
딕셔너리 사용법 : example = {} / example.items() / example[0] = (a,b,c) / example.pop(uid)
for문 변수 두개로 받아오기 : for time, user_id in request:
'''
def process_requests(n, a, b, request):
    storage = {}  # 현재 저장된 유저 정보 {id: (최근 접속 시간, 자리비움 시작 시간, 삭제 시간)}
    result = []
    
    for time, user_id in request:
        # 시간 경과에 따라 유저 상태 업데이트
        to_remove = [uid for uid, (start_time, _, _) in storage.items() if start_time + b <= time]
        '''
        to_remove = []
        for uid, (start_time, _, _) in storage.items():
            if start_time + b <= time:
                to_remove.append(uid)
        '''
        for uid in to_remove:
            storage.pop(uid)

        if user_id in storage:
            # 기존에 있는 유저는 시간만 갱신
            start_time = time
            idle_time = start_time + a
            end_time = start_time + b
            storage[user_id] = (start_time, idle_time, end_time)
            result.append(len(storage)) 
            continue
        
        if len(storage) < n:
            # 저장 공간이 남아있다면 추가
            start_time = time
            idle_time = start_time + a
            end_time = start_time + b
            storage[user_id] = (start_time, idle_time, end_time)
            result.append(len(storage))
        else:
            # 가장 오래 자리비운 유저 찾기
            idle_candidates = [(idle_time, uid) for uid, (start_time, idle_time, _) in storage.items() if idle_time <= time]
            '''
            idle_candidates = []
            for uid, (start_time, idle_time, _) in storage.items():
                if idle_time <= time:
                    idle_candidates.append((idle_time, uid))
            '''
            idle_candidates.sort()
            
            if idle_candidates:
                # 자리비운 유저 제거 후 새로운 유저 추가
                kicked_user = idle_candidates[0][1]
                storage.pop(kicked_user, None)
                
                start_time = time
                idle_time = start_time + a
                end_time = start_time + b
                storage[user_id] = (start_time, idle_time, end_time)
                result.append(len(storage))
            else:
                # 자리비운 유저가 없다면 -1 리턴
                result.append(-1)
        
    return result

# 테스트 예제
'''
n = 2
a = 10
b = 100
request = [[2,1000],[3,1001],[4,1005],[8,1000],[12,1002],[13,1002],[14,1001],[200,1301]]
'''
n = 5
a = 100
b = 200
request = [[11,1],[12,2],[13,1],[16,3],[200,1],[214,1],[216,1]]

print(process_requests(n, a, b, request))
