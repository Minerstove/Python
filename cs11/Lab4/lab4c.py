def make_poetic(poem, synonyms):

    graph = {}
    for a, b in synonyms:
        graph.setdefault(a, set()).add(b)
        graph.setdefault(b, set()).add(a)

    longest_synonym_dict = {}
    for word in graph:
        checking =  sorted([word] + list(graph[word]))
        longest_synonym_dict[word] = max(checking, key=len)

    words = poem.split()
    for i in range(len(words)):
        if words[i] in longest_synonym_dict:
            words[i] = longest_synonym_dict[words[i]]

    return " ".join(words)

assert make_poetic("i think that i shall never see a poem as lovely as a tree", (
    ('think', 'ruminate'), ('vista', 'view'), ('think', 'conjecture'), ('hypothesize', 'conjecture'),
    ('think', 'guess'), ('wealth', 'cornucopia'), ('panorama', 'scenery'), ('theorize', 'conjecture'),
    ('suppose', 'think'), ('feel', 'think'), ('lovely', 'mesmerizing'), ('think', 'suspect'),
    ('scenery', 'landscape'), ('guess', 'conjecture'), ('tree', 'willow'), ('glimpse', 'see'),
    ('poem', 'ode'), ('will', 'intent'), ('lovely', 'enchanting'), ('think', 'doubt'), ('oak', 'tree'),
    ('beautiful', 'lovely'), ('lovely', 'bewitching'), ('see', 'view'), ('doubt', 'question'),
    ('topography', 'scenery'), ('think', 'muse'), ('surroundings', 'scenery'), ('see', 'discern'),
    ('think', 'reckon'), ('lovely', 'picturesque'), ('observe', 'see'), ('think', 'ponder'),
    ('discern', 'distinguish'), ('think', 'surmise'), ('will', 'shall'), ('suspect', 'defendant'),
    ('will', 'resolve'), ('believe', 'think'), ('view', 'scenery'), ('pulchritudinous', 'lovely'),
    ('suspect', 'theorize'), ('believe', 'trust'), ('see', 'notice'), ('sea', 'ocean'),
)) == "i conjecture that i shall never discern a poem as pulchritudinous as a willow", make_poetic("i think that i shall never see a poem as lovely as a tree", (
    ('think', 'ruminate'), ('vista', 'view'), ('think', 'conjecture'), ('hypothesize', 'conjecture'),
    ('think', 'guess'), ('wealth', 'cornucopia'), ('panorama', 'scenery'), ('theorize', 'conjecture'),
    ('suppose', 'think'), ('feel', 'think'), ('lovely', 'mesmerizing'), ('think', 'suspect'),
    ('scenery', 'landscape'), ('guess', 'conjecture'), ('tree', 'willow'), ('glimpse', 'see'),
    ('poem', 'ode'), ('will', 'intent'), ('lovely', 'enchanting'), ('think', 'doubt'), ('oak', 'tree'),
    ('beautiful', 'lovely'), ('lovely', 'bewitching'), ('see', 'view'), ('doubt', 'question'),
    ('topography', 'scenery'), ('think', 'muse'), ('surroundings', 'scenery'), ('see', 'discern'),
    ('think', 'reckon'), ('lovely', 'picturesque'), ('observe', 'see'), ('think', 'ponder'),
    ('discern', 'distinguish'), ('think', 'surmise'), ('will', 'shall'), ('suspect', 'defendant'),
    ('will', 'resolve'), ('believe', 'think'), ('view', 'scenery'), ('pulchritudinous', 'lovely'),
    ('suspect', 'theorize'), ('believe', 'trust'), ('see', 'notice'), ('sea', 'ocean'),
))


