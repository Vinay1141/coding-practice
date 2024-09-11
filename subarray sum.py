import math
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
marr = -math.inf  
sm = 0
i = 0
while i < len(arr): 
    sm += arr[i]
    marr = max(sm, marr)  
    if sm < 0:
        sm = 0 
    i += 1 
print(marr)
