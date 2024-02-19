def solution(n):
    nlist = []
    
    while n != 1:
        nlist.append(int(n))
        if n % 2 == 0:
            n = n / 2
        else:
            n = n*3+1
    nlist.append(1)
    
    return nlist

        
