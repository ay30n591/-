def solution(numLog):
    result = ""
    for i in range(1,len(numLog)):
        var = numLog[i] - numLog[i-1]
        if var == 1:
            result =result+"w"
        elif var == -1:
            result =result+"s"
        elif var == 10:
            result = result+"d"
        else:
            result = result+"a"
    return result