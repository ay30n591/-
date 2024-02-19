def solution(arr, queries):
    result = []
    tmp = []
#     for s, e, k in queries:
#         found = False  # 조건에 맞는 값이 있는지 여부를 나타내는 변수
#         for i in range(s, e + 1):
#             if i > k:
#                 result.append(i)
#                 found = True
#                 break  # 조건을 만족하는 값을 찾았으면 더 이상 확인할 필요 없음
#         if not found:
#             result.append(-1)  # 조건을 만족하는 값을 찾지 못한 경우 -1 추가
#     return result
    
    for s,e,k in queries:
        tmp = list(filter(lambda x : x > k, sorted(arr[s:e+1])))
        if len(tmp) > 0:
            result.append(tmp[0])
        else:
            result.append(-1)
    return result
 
#     for s,e,k in queries:
#         for i in range(s,e+1):
#             if i > k :
#                 if min(i):
#                     result.append(i)
#             else:
#                 result.append(-1)
                    
#     return result