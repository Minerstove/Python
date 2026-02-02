import sys
sys.setrecursionlimit(4000)

#there are no cases for Subtask 3 and 4. i did not have time to make them :(

#put your solution here
#i can't check constraints, so just be honest hehe

#---to test your code, RUN this file---
def sugar_rush_racetrack(n,r,c):
    
    def path_finder(current_tile, r, c, status, n, minr, minc):
        if n == 0:
            return current_tile
        
        row, column = current_tile[0], current_tile[1]
        
        if status == "RIGHT":
            # print(current_tile)
            # print(status)
            # steps available from (row, column) to the right edge
            if n <= len(range(column + 1, c)):
                return (row, column + n)
            # hit right edge; consume exactly len(range(column+1, c)) steps
            return path_finder((row, c - 1), r, c, "DOWN",
                               n - len(range(column + 1, c)),
                               minr + 1, minc)

        if status == "DOWN":
            # print(current_tile)
            # print(status)
            if n <= len(range(row + 1, r)):
                return (row + n, column)
            # hit bottom edge; shrink right boundary (c -> c-1)
            return path_finder((r - 1, column), r, c - 1, "LEFT",
                               n - len(range(row + 1, r)),
                               minr, minc)

        if status == "LEFT":
            # print(current_tile)
            # print(status)
            if n <= len(range(minc, column)):
                return (row, column - n)
            # hit left edge; shrink bottom boundary (r -> r-1)
            return path_finder((row, minc), r - 1, c, "UP",
                               n - len(range(minc, column)),
                               minr, minc)

        if status == "UP":
            #print(current_tile)
            #print(status)
            if n <= len(range(minr, row)):
                return (row - n, column)
            # hit top edge; consume steps and then move RIGHT next; minc -> minc+1
            return path_finder((minr, column), r, c, "RIGHT",
                               n - len(range(minr, row)),
                               minr, minc + 1)
            
    return path_finder((0, 0), r, c, "RIGHT", n, 0, 0)
    

#print(sugar_rush_racetrack(19,5,4))
#print(sugar_rush_racetrack(0, 1, 1))
#print(sugar_rush_racetrack(10, 10, 10))
#print(sugar_rush_racetrack(20, 20, 20))

#---to test your code, RUN this file---

if __name__ == "__main__":
    from tester import run_tests
    run_tests()

"""
brute force solution
def path_finder(current_tile, r, c, status, visited, n, current_step, minr, minc):
        if current_step == n:
            return current_tile
        
        row, column = current_tile[0], current_tile[1]
        
        if status == "RIGHT":
            print(current_tile)
            print(status)
            if column <= (c - 1):
                column = column + 1
                visited = visited + (row, column)
                return path_finder((row, column), r, c, "RIGHT", visited, n, current_step + 1, minr, minc)
            else:
                row = row + 1
                visited = visited + (row, column)
                return path_finder((row, column), r, c, "DOWN", visited, n, current_step + 1, minr + 1, minc)

        if status == "DOWN":
            print(current_tile)
            print(status)
            if row <= (r - 1):
                row = row + 1
                visited = visited + (row, column)
                return path_finder((row, column), r, c, "DOWN", visited, n, current_step + 1, minr, minc)
            else:
                column = column - 1
                visited = visited + (row, column)
                return path_finder((row, column), r, c - 1, "LEFT", visited, n, current_step + 1, minr, minc)

        if status == "LEFT":
            print(current_tile)
            print(status)
            if column > minc:
                column = column - 1
                visited = visited + (row, column)
                return path_finder((row, column), r, c, "LEFT", visited, n, current_step + 1, minr, minc)
            else:
                row = row - 1
                visited = visited + (row, column)
                return path_finder((row, column), r - 1, c, "UP", visited, n, current_step + 1, minr, minc)
            
        if status == "UP":
            print(current_tile)
            print(status)
            if row > minr:
                row = row - 1
                visited = visited + (row, column)
                return path_finder((row, column), r, c, "UP", visited, n, current_step + 1, minr, minc)
            else:
                column = column + 1
                visited = visited + (row, column)
                return path_finder((row, column), r, c, "RIGHT", visited, n, current_step + 1, minr, minc + 1)
            
    return path_finder((0, 0), r - 1, c - 1, "RIGHT", ((0,0),), n, 0, 0, 0)
"""