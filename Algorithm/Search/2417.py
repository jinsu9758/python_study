n = int(input())

start = 0
end = n

while start <= end:
    middle = (start+end)//2
    if middle**2 < n:
        start = middle + 1
    else:
        end = middle - 1
print(start)
