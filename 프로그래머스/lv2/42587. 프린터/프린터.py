from collections import deque

def solution(priorities, location):
    answer = 0
    
    prior_list = enumerate(priorities)
    deq = deque(prior_list)
    
    print(deq)
    
    while True:
        max_priority = max([b for a, b in deq])
        
        if deq[0][1] >= max_priority:
            if deq[0][0] == location:
                answer += 1
                return answer
            deq.popleft()
            answer += 1

        else:
            deq.append(deq.popleft())
