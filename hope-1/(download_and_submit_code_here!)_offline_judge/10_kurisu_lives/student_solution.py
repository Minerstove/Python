#put your solution here
#i can't check constraints, so just be honest hehe

#---to test your code, RUN this file---
def kurisu_lives(tl, k, n):
    m = len(tl)

    if k == 0:
        return "Convergence" if n == 0 else "Divergence"
    if k > m:
        return "Divergence"

    def exists(start, need, target):
        if need == 0:
            return target == 0
        if m - start < need:
            return False
        #print(f"start={start}, need={need}, target={target}, choices={list(range(start, m-(need-1)))}")
        return any(
            exists(i + 1, need - 1, target - tl[i])
            for i in range(start, m - (need - 1))
        )

    return "Convergence" if exists(0, k, n) else "Divergence"

# print(kurisu_lives((1, 2, 3), 2, 3)) # Convergence
# print(kurisu_lives((10, 20, 30), 2, 25)) # Divergence
# print(kurisu_lives((2, -1, 4), 1, 2)) # Convergence
# print(kurisu_lives((1, 2, 3, 4), 4, 11))

#---to test your code, RUN this file---

if __name__ == "__main__":
    from tester import run_tests
    run_tests()