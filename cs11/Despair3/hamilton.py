hamilton = list(map(int, input().split()))
quezon = list(map(int, input().split()))
reform = list(map(int, input().split()))

def bs(freedom, arr):
    lo = 0
    hi = len(arr)

    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] >= freedom:
            hi = mid
        else:
            lo = mid + 1

    return lo

prefix_sums = []
owners = []
i = 0
j = 0
total = 0
turn = 0

while True:
    moved = False
    
    if i < len(hamilton):
        total += hamilton[i]
        i += 1
        prefix_sums.append(total)
        owners.append("HAMILTON")
        moved = True

    # then QUEZON
    if j < len(quezon):
        total += quezon[j]
        j += 1
        prefix_sums.append(total)
        owners.append("QUEZON")
        moved = True

    if not moved:  # both exhausted
        break
    
for freedom in reform:
    idx = bs(freedom, prefix_sums)
    if idx < len(prefix_sums):
        print(owners[idx])
    else:
        print("NONE")

# for freedom in reform:
#     it1 = iter(hamilton)
#     it2 = iter(quezon)

#     freedom_meter = 0
#     current = None
    

#     while True:
#         moved = False

#         try:
#             freedom_meter += next(it1)
#             current = "HAMILTON"
#             moved = True
#         except StopIteration:
#             pass
        
#         if freedom_meter >= freedom:
#             break

#         try:
#             freedom_meter += next(it2)
#             current = "QUEZON"
#             moved = True
#         except StopIteration:
#             pass

#         if freedom_meter >= freedom:
#             break

#         if not moved:
#             break
        
#     if freedom_meter >= freedom:
#         print(current)
#     else:
#         print("NONE")
