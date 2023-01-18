def solution(s):
    # 이건 stack이다..! 
    
    stack = []
    
    for ele in s:
        if stack:
            if ele == stack[-1]:
                #stack.pop(ele)
                del stack[-1]
            else:    
                stack.append(ele)
        else: 
            stack.append(ele)
                
    if stack:
        return 0
    else:
        return 1