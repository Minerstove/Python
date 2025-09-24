
def sugar_rush_racetrack(n,r,c):
    try:
        try:
            def rec(n,c1,c2):
                top,left = c1 
                bottom,right = c2

                if n==0: return (top,left)

                #checking each corner
                steps = right-left 
                if n<=steps: return(top, left+n)
                n -= steps

                steps = bottom-top
                if n<=steps: return(top+n, right)
                n -= steps

                steps = right-left
                if n<=steps: return(bottom, right-n)
                n -= steps

                steps = bottom-top
                if n+1 <=steps: return (bottom-n, left) #'+1' because we don't want to reconsider the topleft corner in count
                n -= steps

                #make rectangle smaller
                top+=1
                right-=1
                bottom-=1
                left+=1
            
                return rec(n,(top,left),(bottom,right))
            return rec(n,(0,0),(r-1,c-1))
        except:
            raise NotImplementedError(
            "Subtask doesn't have cases! I didn't have time to make the solution for this subtask :("
        )
    except:
        raise NotImplementedError(
        "Subtask doesn't have cases! I didn't have time to make the solution for this subtask :("
    )