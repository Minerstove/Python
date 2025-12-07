def identify_strongest(put_in_match, names):
    names = list(names)
    defeats = {}
    
    def bracket(names):
        current = names
        while len(current) > 1:
            next_round = []
            for i in range(1, len(current), 2):
                winner = put_in_match(current[i], current[i - 1])
                loser = current[i] if winner != current[i] else current[i - 1]
                defeats.setdefault(winner, []).append(loser)
                next_round.append(winner)

            if len(current) % 2 == 1:
                next_round.append(current[-1])
            
            current = next_round    
        return winner
    
    winner = bracket(names)
    second = bracket(defeats[winner])

    return (winner, second)
    

def put_in_match(val1, val2):
    return val2


assert identify_strongest(put_in_match, ("Magikarp", "Pikachu", "Bulbasaur", "Ditto")) == ("Magikarp", "Bulbasaur"), identify_strongest(put_in_match, ("Magikarp", "Pikachu", "Bulbasaur", "Ditto"))

print(identify_strongest(put_in_match, ("1", "2", "3", "4", "5", "6")))

# def identify_strongest(put_in_match, names): only works for 2^n names
#     names = list(names)
#     defeats = {}

#     while len(names) > 1:
#         for i in range(1, len(names), 2):
#             winner = put_in_match(names[i], names[i - 1])
#             loser = names[i] if winner != names[i] else names[i - 1]
#             defeats.setdefault(winner, []).append(loser)

#             if winner == names[i]:
#                 names[i - 1] = 0
#             else:
#                 names[i] = 0

#         names = list(filter(lambda x: x != 0, names))
    
#     second_place_candidates = defeats[winner]
#     second = second_place_candidates[0]

#     while len(second_place_candidates) > 1:
#         for i in range(1, len(second_place_candidates), 2):
#             second = put_in_match(second_place_candidates[i], second_place_candidates[i - 1])
#             loser2 = second_place_candidates[i] if second != second_place_candidates[i] else second_place_candidates[i - 1]

#             if second == second_place_candidates[i]:
#                 second_place_candidates[i - 1] = 0
#             else:
#                 second_place_candidates[i] = 0

#         second_place_candidates = list(filter(lambda x: x != 0, second_place_candidates))

#     return (winner, second)