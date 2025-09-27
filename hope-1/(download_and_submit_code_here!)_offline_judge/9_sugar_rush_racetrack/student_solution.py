import sys
sys.setrecursionlimit(4000)

#there are no cases for Subtask 3 and 4. i did not have time to make them :(

#put your solution here
#i can't check constraints, so just be honest hehe

#---to test your code, RUN this file---
def sugar_rush_racetrack(n,r,c):

    def in_bounds(i, j):
        return 0 <= i < r and 0 <= j < c
    
    def path_finder(current_tile, r, c, status, visited, n, current_step, minr, minc):
        if current_step == n:
            return current_tile
        
        row, column = current_tile[0], current_tile[1]
        
        if status == "RIGHT":
            if column <= (c - 1):
                column = column + 1
                visited = visited + (row, column)
                return path_finder((row, column), r, c, "RIGHT", visited, n, current_step + 1, minr, minc)
            else:
                row = row + 1
                visited = visited + (row, column)
                return path_finder((row, column), r, c, "DOWN", visited, n, current_step + 1, minr + 1, minc)

        if status == "DOWN":
            if row <= (r - 1):
                row = row + 1
                visited = visited + (row, column)
                return path_finder((row, column), r, c, "DOWN", visited, n, current_step + 1, minr, minc)
            else:
                column = column - 1
                visited = visited + (row, column)
                return path_finder((row, column), r, c - 1, "LEFT", visited, n, current_step + 1, minr, minc)

        if status == "LEFT":
            if column > minc:
                column = column - 1
                visited = visited + (row, column)
                return path_finder((row, column), r, c, "LEFT", visited, n, current_step + 1, minr, minc)
            else:
                row = row - 1
                visited = visited + (row, column)
                return path_finder((row, column), r - 1, c, "UP", visited, n, current_step + 1, minr, minc)
            
        if status == "UP":
            if row > minr:
                row = row - 1
                visited = visited + (row, column)
                return path_finder((row, column), r, c, "UP", visited, n, current_step + 1, minr, minc)
            else:
                column = column + 1
                visited = visited + (row, column)
                return path_finder((row, column), r, c, "RIGHT", visited, n, current_step + 1, minr, minc + 1)
            
    return path_finder((0, 0), r, c, "RIGHT", ((0,0),), n, 0, 0, 0)

#print(sugar_rush_racetrack(19,5,4))


#---to test your code, RUN this file---

if __name__ == "__main__":
    from tester import run_tests
    run_tests()
