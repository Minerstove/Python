"""
Indices allow us to access elements through recursion or comprehension
"""

def idx_pairs0(n):
    return tuple((i,j) 
        for j in range (n)
        for i in range (j+1)
    )

