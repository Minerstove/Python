#put your solution here
#i can't check constraints, so just be honest hehe

#---to test your code, RUN this file---
def sudapap(r,j):
    if r == 1 and j == 1:
        return (1,1)
    def hon_counter(r,j,counter):
        if r <= 0:
            return (counter, j)
        if j <= 0:
            return (counter, r)
        
        if r > j:
            this_round_hon = r // j
            counter = counter + this_round_hon
            new_r = r - this_round_hon * j
            return hon_counter(j, new_r, counter)
        elif j > r:
            this_round_hon = j // r
            counter = counter + this_round_hon
            new_j = j - this_round_hon * r
            return hon_counter(r, new_j, counter)
        
    return hon_counter(r, j, 0)

"""print(sudapap(49,7))
print(sudapap(1,1))
print(sudapap(1230,126))"""

#---to test your code, RUN this file---

if __name__ == "__main__":
    from tester import run_tests
    run_tests()