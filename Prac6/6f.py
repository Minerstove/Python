def num_lunch(ulams,drinks):
    ulams = list(ulams)
    drinks = list(drinks)
    paired = 0
    used_ulams = [False] * len(ulams)
    used_drinks = [False] * len(drinks)

    for i in range(len(ulams)):
        for j in range(len(drinks)):
            if not used_ulams[i] and not used_drinks[j]:
                if (ulams[i] + drinks[j]) % 2 != 1:
                    pass
                else:
                    paired += 1
                    used_ulams[i] = True
                    used_drinks[j] = True
    
    return paired


assert num_lunch(
    (3, 1, 4, 1, 5),
    (2, 7, 1, 8, 2),
) == 4, num_lunch(
    (3, 1, 4, 1, 5),
    (2, 7, 1, 8, 2),
)

assert num_lunch(
    (3, 1, 4, 1, 5, 9, 2, 6, 5),
    (2,),
) == 1, num_lunch(
    (3, 1, 4, 1, 5, 9, 2, 6, 5),
    (2,),
)


