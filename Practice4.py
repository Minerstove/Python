#Prac 4a - Shaman II: Shampoo
def jeepney_groups(passengers, jeepney_counts):
    if len(passengers) == 0:
        return ()
    if not jeepney_counts:
        return ()
    return tuple(passengers[sum(jeepney_counts[:i]) : sum(jeepney_counts[:i+1])] for i in range(len(jeepney_counts)))

print(jeepney_groups(('eiko', 'dagger', 'freya', 'amarant', 'vivi', 'steiner', 'zidane', 'quina'), (3, 4, 1)))
print(jeepney_groups((), (3, 4, 1)))
print(jeepney_groups(('eiko', 'dagger', 'freya', 'amarant', 'vivi', 'steiner', 'zidane', 'quina'), ()))