def div_by_9_between(a, b):
    def divisibility(n):
        return n%9==0
    def divide_by_9(num):
        numA = a
        numB = b
        if num > numB:
            return ()
        elif divisibility(num) and numA<=num:
            return (num,) + divide_by_9(num+9)
        else:
            return divide_by_9(num+1)
    return divide_by_9(a)

"""print(div_by_9_between(25, 50))     
print(div_by_9_between(27, 45))
print(div_by_9_between(91, 98))"""

#Prac 1b
def floor_sum(n, a, b)->int: #n/a summed until n/b
    if a==b:
        return n//b
    return n//a + floor_sum(n,a+1,b)

"""print(floor_sum(7, 1, 7))
print(floor_sum(7, 2, 5))"""

def optimized_floor_sum(n, a, b)->int:
    b = min(b, n)
    def solve(k):
        if k <= b:
            return 0
        q = n // k
        r = solve(k, n // q)
        return (r - k + 1) * q + solve(r+1)
    return solve(a)

#Prac 1c
def darts_landed(x1,y1,x2,y2,dart_coords):
    i=0
    x=0
    y=1
    def darts_in(dart_coords,i):
        if i == len(dart_coords): #base case
            return 0
        elif(
            dart_coords[i][x] >= x1 
            and dart_coords[i][y] >= y1 
            and dart_coords[i][x] <= x2 
            and dart_coords[i][y] <= y2
            ):
            return 1 + darts_in(dart_coords, i+1)
        else:
            return 0 + darts_in(dart_coords, i+1)  
            #check if dart pair are inside the range then return 0 or 1 + recursion of the function until dart_counter function base case.
    return darts_in(dart_coords,i)
    #probably gonna recursion over each element in dart coords and just add 1 if in and 0 if out until no more darts coordinates
"""
print(darts_landed(-20, -10, 20, 10, (
    (0, 0),
    (500, 0),
    (1, 1),
)))"""

#Prac 1d - Rednow Eivets
def fix_music(music):
    i=0
    def reverse_music(music, i):
        if i == len(music):
            return () #None does not work with tuples so use ()
        else:
            return reverse_music(music, i+1) + (music[i][::-1],)
    return reverse_music(music, i)
    
"""print(fix_music(((3, 1, 4), (1, 5))))
print(fix_music(((1, 2, 3), (4, 5), (6, 7, 8, 9))))"""

#Prac 1e - ??
def matches(team1, team2):
    i = 0
    def get_pairs(teamA, teamB, i):
        if i==len(teamA) or i==len(teamB):
            return ()
        (partner1, partner2) = (teamA[i], teamB[i])
        return ((partner1, partner2),) + get_pairs(teamA, teamB, i+1)
    return get_pairs(team1, team2, i)
    
"""
print(matches(('Domon', 'Tokiya', 'Fuuko', 'Koganei', 'Recca'),('Noroi', 'Kai', 'Mikoto', 'Joker', 'Kurei'),))
print(matches(('Piccolo', 'Gokuu', 'Monaka', 'Vegeta'),('Frost', 'Botamo', 'Hit', 'Cabba', 'Magetta'),))
"""

#Prac 1f - Rice Price Rise
def buy_cheapest(rice_prices): 
    def cheapest_price(rice_prices): 
        if len(rice_prices) == 1: 
            return rice_prices[0] 
        elif rice_prices[0] <= rice_prices[1]: 
            return cheapest_price(rice_prices[:1] + rice_prices[2:]) 
        elif rice_prices[0] > rice_prices[1]: 
            return cheapest_price(rice_prices[1:]) 
    
    cheapest = cheapest_price(rice_prices)
    
    def rest_of_the_prices(rice_prices, cheapest): 
        if rice_prices == (): 
            return () 
        elif rice_prices[0] == cheapest: 
            return (rice_prices[1:])
        else:
            return (rice_prices[0],) + rest_of_the_prices(rice_prices[1:], cheapest) 
    
    return (cheapest,) + (rest_of_the_prices(rice_prices, cheapest),)

#refactor, inner function to find smallest value then outer function to delete smallest value from tuple

"""print(buy_cheapest((31, 41, 59, 26, 53)))
print(buy_cheapest((33, 11, 44, 11, 55)))
print(buy_cheapest((7, 3, 3, 3)))"""

#Prac 1g- Suspense Sort
def suspense_sort(sorting):
    def higher_lower(sorting): 
        if len(sorting) == 1: 
            return sorting[0]
        elif sorting[0] <= sorting[1]: 
            return higher_lower(sorting[:1] + sorting[2:]) 
        elif sorting[0] > sorting[1]: 
            return higher_lower(sorting[1:])
    if sorting == ():
        return ()
    
    minimum = higher_lower(sorting)
    
    def rest_of_the_prices(sorting, minimum):
        if sorting == ():
            return ()
        if sorting[0] == minimum:
            return sorting[1:]
        return (sorting[0],) + rest_of_the_prices(sorting[1:], minimum)

    remainder = rest_of_the_prices(sorting, minimum)
    
    return (minimum,) + suspense_sort(remainder)

print(suspense_sort((3, 1, 4, 1, 5)))

#Prac 1h - Transpose Matrix
def transpose(matrix):
    if len(matrix[0][0]) == 1: #base case
        return matrix 
    elif matrix:
        return ... #first row of matrix should become first elements in each row of matrix

"""
Current idea is to recurse on each first element of the column for the transformed first row, 
then do it for each element of the column.

matrices are c x r so while len of matrix (which is the number of columns), each row gets the first element of each item in the matrix
"""