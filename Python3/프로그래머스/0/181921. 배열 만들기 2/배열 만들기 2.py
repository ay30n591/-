def solution(l, r):
    an = []
    for i in range(l,r+1):
        if all(num in ['0','5'] for num in str(i)):
            an.append(i)
            
    if len(an) == 0:
        an.append(-1)
        
    return an

