import sys
sys.setrecursionlimit(300000)

#put your solution here
#i can't check constraints, so just be honest hehe

#---to test your code, RUN this file---
def mkns_2(M,ML,TL,MI):

    def find_intersections(tup1, tup2):

        intersection = tuple(frozenset(tup1) & frozenset(tup2))

        return tuple(msg for msg in M if msg in intersection)
    
    delulu = find_intersections(ML,TL)
    may_chance = find_intersections(TL,MI)
    wag_red_flag = find_intersections(MI,ML)

    return((delulu, may_chance, wag_red_flag))

#---to test your code, RUN this file---

if __name__ == "__main__":
    from tester import run_tests
    run_tests()