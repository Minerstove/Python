#Prac 3a - Bacteria
def bacteria_counts(b, n):
    return tuple(b * 2**i for i in range(n))

#print(bacteria_counts(3, 4)) # == (3, 6, 12, 24)

#Prac 3b - Shaman
def jeepney_groups(passengers, p):
    return tuple(tuple(passengers[i:i + p]) for i in range(0, len(passengers), p))

#print(jeepney_groups(('eiko', 'dagger', 'freya', 'amarant', 'vivi', 'steiner', 'zidane', 'quina'), 2))
#print(jeepney_groups(('eiko', 'dagger', 'freya', 'amarant', 'vivi', 'steiner', 'zidane', 'quina'), 3))

#Prac 3d - Thy Neighbors

def house_locations(distances):
    return (0,) + tuple(sum(distances[0:i]) + distances[i] for i in range(0, len(distances)))

#print(house_locations((2, 7, 1, 8)))

#Prac 3f - Attendance
#Easy Cases
def attendance_easy(attended, class_list):
    return tuple(i for i in class_list if i in attended), tuple(i for i in class_list if i not in attended and class_list)
#When asked to iterate over something to keep an order, make sure to iterate over the thing that you need it ordered by

#Hard Cases O(m + n)
def attendance_hard(attended, class_list):
    attended_dict = {name: True for name in attended}   # O(n)
    class_dict    = {name: True for name in class_list} # O(m)

    in_class_order = tuple(name for name in class_list if name in attended_dict)
    not_in_class   = tuple(name for name in class_list if name not in attended_dict and class_dict)

    return (in_class_order, not_in_class)

print(attendance_easy(
        ('dennis', 'jeremiah', 'eugene'),
        ('eugene', 'alfred', 'dennis', 'vincent'),
    ))

#Prac 3h - School Sections
def empty_sections(s, student_numbers):
    existing_sections = frozenset(i % s for i in student_numbers) 
    return s - len(existing_sections)

"""print(empty_sections(8, (
    200062361, 200000263, 200092785, 200000916, 200071571,
    200089503, 200035712, 200015911, 200070711, 200061120,
    200020828, 200098139, 200056057, 200075391, 200016588,
    200005853, 200090523, 200015692, 200006517, 200066676,
)),)"""

#Prac 3i - I know some of these words
def used_buzz_words(buzz_words, speech):
    return tuple(i for i in buzz_words if i in speech)

"""print(used_buzz_words((
        'quantum',
        'scheme',
        'stack',
        'cohomology',
        'qubits',
        'grassmannian',
        'nullstellensatz',
    ),
    'quantum cellular homology not a mistacke qubitscheme quantumhealing quantum quantum woohoo',
))"""

#Prac 3j - Mag-exercise Tayo Tuwing Umaga
def fitness_routine(exercises):
    ...

