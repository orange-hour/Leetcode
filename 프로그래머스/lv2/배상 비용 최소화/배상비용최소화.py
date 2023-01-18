from heapq import heappush, heappop

def solution(no, works):
    work_heap = []    
    for num in works:
        heappush(work_heap, -num) #최대 힙으로 만들기 위해 음수를 취해준다
    
    for i in range(no):
        new_min = heappop(work_heap) + 1
        heappush(work_heap, new_min)
        
        if i >= sum(works): #만약 i가 no보다 크거나 같다면, loop에서 탈춣해야 한다 (남은 작업을 모두 수행했기 때문)
            return 0
        
    left_work_sum = sum([x**2 for x in work_heap])

    return left_work_sum
