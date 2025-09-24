subtasks = {
    "Subtask 1 (small, distinct messages)" : {
        "points": 100,
        "cases": [
            (
              ("update me v.v", "the moon is beautiful isnt it", "hays", "i luv u <3", "ok", "ih", "mkns"),
              ("ih", "ok", "mkns", "hays"),
              ("mkns", "hays", "update me v.v","i luv u <3"),
              ("update me v.v", "ok","mkns", "i luv u <3", "the moon is beautiful isnt it")
            ),
            (
              ("hi", "ok", "gn"),
              ("hi", "ok"),
              ("ok", "gn"),
              ("hi", "gn", "ok")
            ),
        ]
    },
    "Subtask 2 (large, distinct messages, up to 10000)" : {
        "points": 100,
        "cases": [
                (
                tuple("a" + str(i) for i in range(1, 100001)) +
                tuple("b" + str(i) for i in range(1, 100001)) +
                tuple("c" + str(i) for i in range(1, 100001)),

                tuple("a" + str(i) for i in range(1, 50001)) + ('royrt',) +
                tuple("b" + str(i) for i in range(1, 50001)),

                tuple("b" + str(i) for i in range(1, 50001)) + ('royr3t', 'eoroeor',) +
                tuple("c" + str(i) for i in range(1, 50001)),

                tuple("a" + str(i) for i in range(1, 50001)) + ('royrt',) +
                tuple("c" + str(i) for i in range(1, 50001))
            ),
            (
                tuple('a'+str(i) for i in range(1,50000)),   # M = 10k
                tuple('b'+str(i) for i in range(1,50000)),   # ML = 50k
                tuple('a'+str(i) for i in range(50000,90000)),  # TL = 4k
                tuple('b'+str(i) for i in range(10000,20000))   # MI = 1k
            ),
        ]
        
    },
    "Subtask 3 (with duplicates, long) (I DIDNT MAKE TEST CASES FOR THIS, SO IT WONT GRADE YOU)" : {
        "points": 200,
        "cases": [
            (
              tuple(["ily"]*200 + ["ok"]*150 + ["brb"]*100),
              tuple(["ily"]*200 + ["ok"]*150 + ["brb"]*100),  # ML same as M for coverage
              tuple(["ok"]*100 + ["ily"]*200 + ["gn"]*50),
              tuple(["brb"]*150 + ["ily"]*200 + ["ok"]*100)
            ),
            (
              tuple(["m"]*300 + ["n"]*300 + ["x"]*300),
              tuple(["m"]*200 + ["n"]*200 + ["x"]*200),
              tuple(["n"]*310 + ["m"]*310 + ["x"]*202),
              tuple(["x"]*300 + ["m"]*10 + ["n"]*300)
            ),
        ]
    },
}
