def gas_stations(stations, points):
    if not stations:
        return [None] * len(points)
    
    result = []
    sorted_dict = sorted(stations)

    # BINARY SEARCH
    for point in points:
        left, right = 0, len(sorted_dict) - 1
        ans = None
        while left <= right:
            mid = (left + right) // 2
            if point >= sorted_dict[mid]:
                left = mid + 1
            else:
                ans = sorted_dict[mid]
                right = mid - 1
        result.append(stations[ans] if ans is not None else None)

    return result

assert gas_stations({ 
    555: 'Caltech',
    241: 'Shill',
    214: 'Shill', 
    143: 'Caltech',
    69: 'Patron',
    420: 'Patron',
    42: 'Shill', 
}, (314, 42, 32, 2048, 64, 42, 101)) == [
    'Patron',
    'Patron',
    'Shill',
    None,
    'Patron',
    'Patron',
    'Caltech',
], gas_stations({ 
    555: 'Caltech',
    241: 'Shill',
    214: 'Shill', 
    143: 'Caltech',
    69: 'Patron',
    420: 'Patron',
    42: 'Shill', 
}, (314, 42, 32, 2048, 64, 42, 101))
