def people_inside(logs):
    inside = 0
    result = []
    dictionary = {}

    for person in logs:
        dictionary[person] = dictionary.get(person, "outside")
        if dictionary[person] == "inside":
            dictionary[person] = "outside"
            inside -= 1
            result.append(inside)
        elif dictionary[person] == "outside":
            dictionary[person] = "inside"
            inside += 1
            result.append(inside)

    return result

assert people_inside((
    'Kevin',
    'Rich',
    'Jem',
    'Kevin',
    'Kevin',
    'Jem',
    'Kevin',
    'Jozelle',
    'Kevin',
    'Kevin',
)) == [1, 2, 3, 2, 3, 2, 1, 2, 3, 2], people_inside((
    'Kevin',
    'Rich',
    'Jem',
    'Kevin',
    'Kevin',
    'Jem',
    'Kevin',
    'Jozelle',
    'Kevin',
    'Kevin',
))

