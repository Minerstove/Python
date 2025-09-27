import sys
sys.setrecursionlimit(4000)

#there are no cases for Subtask 3 and 4. i did not have time to make them :(

#put your solution here
#i can't check constraints, so just be honest hehe

#---to test your code, RUN this file---
def sugar_rush_racetrack(n,r,c):

    def in_bounds(i, j):
        return 0 <= i < r and 0 <= j < c
    
    def path_finder(current_tile, r, c, status, visited, n, current_step):
        
        row, column = current_tile[0], current_tile[1]

        if status == "RIGHT":
            if column < c:
                ...
        
        if status == "DOWN":
            if row < r:
                ...

        if status == "LEFT":
            if column < c:
                ... #add cells going left
            
        if status == "UP":
            if row < r:
                ... #add cells going up



    return path_finder((0, 0), r, c, "RIGHT", ((0,0),), n, 0)



#---to test your code, RUN this file---




if __name__ == "__main__":
    from tester import run_tests
    run_tests()