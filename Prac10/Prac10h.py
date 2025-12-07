from functools import cache
from collections import deque

# def sorted_packages(labels, case_sensitive=True):
#     if not case_sensitive:
#         labels = [label.lower() for label in labels]
    
#     s_labels = deque()
    
#     @cache
#     def recursive_sort(labels, index, s_labels):
        
        
#         if labels[index - 1] >= labels[index]:
#             s_labels.appendleft(index - 1)
#         else:
#             s_labels.append(index)

#         if index == len(labels):
#             return s_labels
        
#         s_labels = recursive_sort(labels, index + 1, s_labels)

#     result = recursive_sort(labels, 1, [])

#     return result

def sorted_packages(labels, case_sensitive=True):
    if case_sensitive:
        key_labels = labels
    else:
        key_labels = [label.lower() for label in labels]

    indices = list(range(len(labels)))

    indices.sort(key=lambda i: key_labels[i])

    return indices


assert sorted_packages([
    'iPhone',
    'iPHONE',
    'USB converter',
    'Flash Drive',
    'J Ball speaker',
    'uPhone',
    'cooking pot',
    'headset cup holder',
    'insect racket',
]) == [3, 4, 2, 6, 7, 1, 0, 8, 5], sorted_packages([
    'iPhone',
    'iPHONE',
    'USB converter',
    'Flash Drive',
    'J Ball speaker',
    'uPhone',
    'cooking pot',
    'headset cup holder',
    'insect racket',
])

assert sorted_packages([
    'iPhone',
    'iPHONE',
    'USB converter',
    'Flash Drive',
    'J Ball speaker',
    'uPhone',
    'cooking pot',
    'headset cup holder',
    'insect racket',
], case_sensitive=False) == [6, 3, 7, 8, 0, 1, 4, 5, 2], sorted_packages([
    'iPhone',
    'iPHONE',
    'USB converter',
    'Flash Drive',
    'J Ball speaker',
    'uPhone',
    'cooking pot',
    'headset cup holder',
    'insect racket',
], case_sensitive=False)


