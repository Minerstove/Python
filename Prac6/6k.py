def cheapest_deliveries(s):
    n = len(s)
    possible_lists = [[] for _ in range(n)]
    places_with_stations = []

    for i in range(len(s)):
        if s[i] > 0:
            places_with_stations.append(i)
    
    #get prices before i
    for j in places_with_stations:
        for k in range(len(s[:j])):
            possible_lists[k] += [s[j] + (j - k)*100]

    #get prices after i
    for j in places_with_stations:
        for k in range(len(s[j:])):
            possible_lists[k + j] += [s[j] + (k)*100]

    return [min(x) for x in possible_lists]

assert cheapest_deliveries((0, 1000, 0, 0, 0, 1000, 0, 0, 1000, 0, 0)) == [1100, 1000, 1100, 1200, 1100, 1000, 1100, 1100, 1000, 1100, 1200], cheapest_deliveries((0, 1000, 0, 0, 0, 1000, 0, 0, 1000, 0, 0))

assert cheapest_deliveries((0, 1000, 0, 0, 0, 10000, 0, 0, 1000, 0, 0)) == [1100, 1000, 1100, 1200, 1300, 1300, 1200, 1100, 1000, 1100, 1200], cheapest_deliveries((0, 1000, 0, 0, 0, 10000, 0, 0, 1000, 0, 0))




