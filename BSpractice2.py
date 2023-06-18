from collections import deque

def solution(arr:list):
    ## print lint
    print(arr)
    arr = deque(arr)
    answer = ""
    to_return = ""
    i = 0
    oldt = ""
    while arr:
        t = arr.popleft()
        if t == "BOOL":
            answer += "#"
            i += 1


        if t == "SHORT":
            # if oldt == "BOOL":
            #      answer += "."
            #      i += 1
            while i % 2 != 0:
                answer += "."
                i += 1
            answer += "##"
            i += 2
            
        if t == "FLOAT":
            # if oldt == "BOOL":
            #      answer += "..."
            #      i += 3
            while i % 4 != 0:
                answer += "."
                i += 1
            answer += "####"
            i += 4        

        if t == "INT":
            while i % 8 !=0:
                    answer += "."
                    i += 1
            answer += "########"
            i += 8

        if t == "LONG":
            while i % 8 !=0:
                    answer += "."
                    i += 1
            answer += "################"
            i += 16
        
        oldt = t
    
    while i % 8 != 0:
         answer += "."
         i += 1
    if i >= 128:
            return "HALT"
    for i in range(0, len(answer), 8):
        to_return += answer[i:i+8] + ','
    return to_return[:-1]




print(solution(["INT", "INT", "BOOL", "SHORT", "LONG"]))
print()
print(solution(["INT", "SHORT", "FLOAT", "INT","BOOL"]))
print()
print(solution(["FLOAT", "SHORT", "BOOL", "BOOL", "BOOL", "INT"]))
print()
print(solution(["BOOL", "LONG", "SHORT", "LONG", "BOOL", "LONG", "BOOL", "LONG", "SHORT", "LONG", "LONG"]))
print()
print(solution(["BOOL"]))
print()
print(solution(["BOOL","LONG","BOOL"]))
print()
print(solution(["BOOL","BOOL","SHORT"]))
print()
print(solution(["BOOL","BOOL","BOOL","FLOAT"]))