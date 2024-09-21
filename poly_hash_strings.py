arr = [4, 2, 1, 3]
ans = []
arr.sort(reverse=True)
mn = float('inf') 
for i in range(len(arr) - 1):
    v = arr[i] - arr[i + 1]
    mn = min(v, mn)
for i in range(len(arr) - 1):
    if arr[i] - arr[i + 1] == mn:
        ans.append((arr[i], arr[i + 1]))

print(sorted(ans))
