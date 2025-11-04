def flower_heights(heights, actions):
    result = []
    add = 0
    prefix = [0]
    for h in heights:
        prefix.append(prefix[-1] + h)
    
    for action in actions:
        if action[0] == "water":
            add += 2
            
        else:
            _, i ,j = action
            i -= 1
            base = prefix[j] - prefix[i]
            days = j - i
            result.append(base + add*days)

    return result
"""
To Try:
collect how much times to water. Then water the specific array that much times for each time.

Try doing a prefix sum

Done
"""
assert flower_heights((3, 1, 4, 1, 5, 9), [
    ('total', 2, 4),
    ('total', 3, 3),
    ('total', 5, 6),
    ('water',),
    ('total', 2, 4),
    ('total', 5, 6),
    ('water',),
    ('water',),
    ('water',),
    ('water',),
    ('water',),
    ('water',),
    ('total', 3, 3),
    ('water',),
]) == [6, 4, 14, 12, 18, 18], flower_heights((3, 1, 4, 1, 5, 9), [
    ('total', 2, 4),
    ('total', 3, 3),
    ('total', 5, 6),
    ('water',),
    ('total', 2, 4),
    ('total', 5, 6),
    ('water',),
    ('water',),
    ('water',),
    ('water',),
    ('water',),
    ('water',),
    ('total', 3, 3),
    ('water',),
])

