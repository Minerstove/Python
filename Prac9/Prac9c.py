def entry_report(entry):
    data_log = {}
    index = 0
    for name, purpose in entry:
        index += 1
        data_log[name] = data_log.get(name, [])
        data_log[name].append(index)

    return data_log

assert entry_report([
    ('Kevin', 'Class'),
    ('Rich', 'Class'),
    ('Jem', 'Research'),
    ('Kevin', 'Aircon'),
    ('Kevin', 'Aircon'),
    ('Jem', 'Aircon'),
    ('Kevin', 'Class kunwari'),
    ('Jozelle', 'Class'),
    ('Kevin', 'Aircon'),
]) == {
    'Jem': [3, 6],
    'Jozelle': [8],
    'Kevin': [1, 4, 5, 7, 9],
    'Rich': [2],
},entry_report([
    ('Kevin', 'Class'),
    ('Rich', 'Class'),
    ('Jem', 'Research'),
    ('Kevin', 'Aircon'),
    ('Kevin', 'Aircon'),
    ('Jem', 'Aircon'),
    ('Kevin', 'Class kunwari'),
    ('Jozelle', 'Class'),
    ('Kevin', 'Aircon'),
])


