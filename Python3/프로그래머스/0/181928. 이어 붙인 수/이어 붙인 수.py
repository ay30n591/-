def solution(num_list):
    aa = ""
    bb = ""
    for i in num_list:
        if  i % 2 == 0 :
            aa += str(i)
        else:
            bb += str(i)
    return int(aa)+int(bb)
      
    

    
