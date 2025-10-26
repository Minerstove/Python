def with_freq_count(string):
    list_string = [word for line in string.split("\n") if line.strip() for word in line.split() if word.strip]
    dict_string = {}
    paired_values = []
    for word in list_string:
        if word in dict_string:
            dict_string[word] = dict_string.get(word, 0)
            dict_string[word] += 1
            paired_values.append((word, dict_string[word]))
        else:
            dict_string[word] = dict_string.get(word, 0)
            paired_values.append((word, dict_string[word]))

    return paired_values

assert with_freq_count("""
don't stop me now
I'm having such a good time
I'm having a ball
don't stop me now
if you wanna have a good time
just give me a call
""") == [
    ("don't", 0),
    ('stop', 0),
    ('me', 0),
    ('now', 0),
    ("I'm", 0),
    ('having', 0),
    ('such', 0),
    ('a', 0),
    ('good', 0),
    ('time', 0),
    ("I'm", 1),
    ('having', 1),
    ('a', 1),
    ('ball', 0),
    ("don't", 1),
    ('stop', 1),
    ('me', 1),
    ('now', 1),
    ('if', 0),
    ('you', 0),
    ('wanna', 0),
    ('have', 0),
    ('a', 2),
    ('good', 1),
    ('time', 1),
    ('just', 0),
    ('give', 0),
    ('me', 2),
    ('a', 3),
    ('call', 0),
], with_freq_count("""
don't stop me now
I'm having such a good time
I'm having a ball
don't stop me now
if you wanna have a good time
just give me a call
""")

assert with_freq_count('a A a A') == [('a', 0), ('A', 0), ('a', 1), ('A', 1)], with_freq_count('a A a A')

