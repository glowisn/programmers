from collections import OrderedDict

def solution(arr:list):
    answer = []
    od = OrderedDict()
    for el in arr:
        if el in od:
            od[el] += 1
        else:
            od[el] = 1
    for key,item in od.items():
        if item != 1:
            answer.append(item)
    return [-1] if len(answer) == 0 else answer



print(solution([]))
print(solution([1,2,3,3,3,3,4,4]))
print(solution([3,2,4,4,2,5,2,5,5]))
print(solution([3,5,7,9,1]))
print(solution([9,9,9,9,8,8,8,7,7]))