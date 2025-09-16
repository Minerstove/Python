#Prac 4a - Shaman II: Shampoo
def jeepney_groups(passengers, jeepney_counts):
    return tuple(passengers[sum(jeepney_counts[:i]) : sum(jeepney_counts[:i+1])] for i in range(len(jeepney_counts)))

"""
print(jeepney_groups(('eiko', 'dagger', 'freya', 'amarant', 'vivi', 'steiner', 'zidane', 'quina'), (3, 4, 1)))
print(jeepney_groups((), (3, 4, 1)))
print(jeepney_groups(('eiko', 'dagger', 'freya', 'amarant', 'vivi', 'steiner', 'zidane', 'quina'), ()))
"""
#Prac 4b - Shaman II: Shampoo

#Prac 4c - Banana Queue
def banana_sequence(flavors):
    return "".join(
        flavors[i // 2] if i % 2 == 0 
        else flavors[-((i + 1) // 2)] 
        for i in range(len(flavors))
        )

"""
print(banana_sequence('saging'))
print(banana_sequence('maypuso'))
print(banana_sequence('petal'))
print(banana_sequence('preserve'))
"""

#Prac 4d - Banana Queue recursively

def banana_sequence2(flavors):

    if len(flavors) == 0:
        return ""
    if len(flavors) == 1:
        return flavors
        
    return flavors[0] + flavors[-1] + banana_sequence2(flavors[1:-1])

"""
print(banana_sequence2('saging'))
print(banana_sequence2('maypuso'))
print(banana_sequence2('petal'))
print(banana_sequence2('preserve'))
"""

#Prac 4e - Ako Ang Nagwagi (Need a more efficient algorithm)
def longest_winning_streak(winners):
    if not winners:
        return 0
    
    def helper(rest, last, cur, best):
        if not rest:
            return best if best > cur else cur
        head = rest[0]
        tail = rest[1:]
        new_cur = cur + 1 if head == last else 1
        new_best = best if best > new_cur else new_cur
        return helper(tail, head, new_cur, new_best)
    
    return helper(winners[1:], winners[0], 1, 1)
"""
print(longest_winning_streak((
        'charlie',
        'charlie',
        'xqc',
        'xqc',
        'charlie',
        'charlie',
        'charlie',
        'charlie',
        'xqc',
        'xqc',
        'charlie',
        'charlie',
    ))
)
"""

#Prac 4f - Defying Gravity

def fall(grid):
    C = len(grid[0])
    R = len(grid)
    
    flipped_grid = tuple(
        "".join(grid[i][j] for i in range(R))
        for j in range(C))
    
    def move_chars_right(input_rows):
        if not input_rows:
            return ()
        blocks = "".join(block for block in input_rows[0] if block != ".")
        fixed_row = "." * (len(input_rows[0]) - len(blocks)) + blocks
        return tuple((fixed_row,)) + tuple(move_chars_right(input_rows[1:]))

    def flip_back(final_grid):
        fixed_grid = tuple(
            "".join(final_grid[j][i] 
            for j in range(len(final_grid)))
            for i in range(len(final_grid[0])))
        return fixed_grid

    return flip_back(move_chars_right(flipped_grid))
"""
print(fall((
    '.X.XX.',
    '.XX...',
    'X...X.',
    '.XXX..',
    '......',
))
)
"""

#Prac 4g - Rotate Painting
def rotate_cw(painting):
    C = len(painting[0])
    R = len(painting)
    
    flipped_grid = tuple(
        "".join(painting[R-1-i][j] for i in range(R))
        for j in range(C))
    
    return flipped_grid
"""
print(rotate_cw((
    '.....-...#.',
    '.####-...#.',
    '.....-...#.',
    '.....-.....',
    '#####-#####',
    '.....-.....',
    '|||||+|||||',
    '.....-.....',
    '.....-#####',
    '.....-.....',
    '.####-#####',
    '.....-.....',
))
)
"""
#Prac 4h - Rotate Painting II
def rotate_cw_k(painting, k):
    equiv_turns = k % 4
    def rotator(painting, turns):
        C = len(painting[0])
        R = len(painting)
        if turns == 0:
            return painting
        flip_grid = tuple(
            "".join(painting[R-1-i][j] for i in range(R))
            for j in range(C))
        return rotator(flip_grid, turns - 1)
    return rotator(painting, equiv_turns)

print(rotate_cw_k((
    '.....|.#....',
    '.#...|.#..#.',
    '.#...|.#..#.',
    '.#...|.#..#.',
    '.#...|.#..#.',
    '-----+------',
    '.#.#.|.#....',
    '.#.#.|.#....',
    '.#.#.|.#....',
    '.#.#.|.#.###',
    '.#.#.|.#....',
), 2)
)
