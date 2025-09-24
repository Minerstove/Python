def trace_square_edge(c1, c2):
    x1,y1=c1
    x2,y2=c2
    x1,x2=min(x1,x2),max(x1,x2)
    y1,y2=min(y1,y2),max(y1,y2)
    a = tuple((i,j) for i in range(x1,x2+1) for j in range(y1,y2+1) if (i==x1 or i==x2) or (j==y1 or j==y2))
    return a

def trace_square_inside(c1, c2):
    x1,y1=c1
    x2,y2=c2
    x1,x2=min(x1,x2),max(x1,x2)
    y1,y2=min(y1,y2),max(y1,y2)
    a = tuple((i,j) for i in range(x1,x2+1) for j in range(y1,y2+1) if not ((i==x1 or i==x2) or (j==y1 or j==y2)))
    return a

def check_square(r,c,rn,cn,grid):
    edge = trace_square_edge((r,c),(rn,cn))
    inside = trace_square_inside((r,c),(rn,cn))
    a = tuple(False for tent_r in range(r,rn+1) for tent_c in range(c,cn+1) if (grid[tent_r][tent_c]!='X' and (tent_r,tent_c) in edge) or (grid[tent_r][tent_c]!=' ' and (tent_r, tent_c) in inside))
    return False not in a

def flood_control(grid):
    R,C = len(grid), len(grid[0])
    count = tuple((i-1)**2
     for r in range(R)
     for c in range(C)
     for i in range(1,min(R-r,C-c))
     if check_square(r,c,r+i,c+i,grid))
    return sum(count)*50