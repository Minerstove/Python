from collections import deque

def rolling_queue(vals):
    vals = deque(vals)
    def f(n):
        
        vals.append(n)
        minimum = min(vals)
        vals.popleft()

        return minimum
    return f