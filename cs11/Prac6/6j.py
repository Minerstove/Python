def bakebook(reqs):
    names = {}
    for req, x in reqs:
        if req == "register":
            if x in names:
                print("already registered")
            else:
                names[x] = []
                print("ok")
        
        if req == "num_friends":
            if x in names:
                print(str(len(names[x])))
            else:
                print("not found")

        if req == "make_friends":
            a, b = x[0], x[1]

            if (a in names and b in names):
                if b == a:
                    print("invalid")
                if b in names[a]:
                    print("already friends")
                else:
                    names[a] = names[a] + [b]
                    names[b] = names[b] + [a]
                    print("ok")
            else:
                print("not found")

bakebook((
    ("num_friends", "gordon"),
    ("register", "gordon"),
    ("num_friends", "gordon"),
    ("register", "ramsey"),
    ("register", "ramsay"),
    ("register", "ramses"),
    ("make_friends", ("gordon", "ramsay")),
    ("make_friends", ("ramsay", "gordon")),
    ("num_friends", "gordon"),
    ("num_friends", "ramses"),
    ("num_friends", "gordan"),
    ("register", "ramsay"),
    ("make_friends", ("gordon", "ramses")),
    ("num_friends", "gordon"),
    ("num_friends", "ramsey"),
    ("make_friends", ("gordon", "gordon")),
    ("make_friends", ("garden", "garden")),
))





# 1st case 
# name: (tuple of friends)
# 2nd case
# 3rd case