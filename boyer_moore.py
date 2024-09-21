import math
a = [3, 3, 2]
c = -1
m = None  
for i in a:
    if c == 0:
        m = i
        c = 1
    elif i == m:
        c += 1
    else:
        c -= 1
print(m)
