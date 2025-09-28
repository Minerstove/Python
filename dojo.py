# ALL RECURSION MUWAHAHAHAHA

# Differences between types of recursion:
# Normal - welp, default one
# Accumulative - uses an accumulative variable as a parameter and use that in the next recursive call
# Mutual - uses another function (maybe in a cycle)

# Takeaways in my case...
# [1] I got used to normal recursion, but I always end up needing to implement concat(value, seq)
# which prepends value to all of in seq, which is inefficient
# as such, I really find the new idea of accumulative recursion very useful (and realize why didn't I think of this before TT)
# [2] I noticed I usually make two types of acc, in-line and in paramater.
# The parameter is most of the time me trying to represent a single solution
# Whereas the in-line acc is the collection of all solutions

# [1] Permutation aka All Reordering
def permutation(seq):
    def _permutation(i, seq, acc):
        if len(seq) == 1:
            return (acc + (seq[0],),)
        if i == len(seq):
            return ()

        return (_permutation(0, remove(seq[i], seq), acc + (seq[i],)) + # All permutations starting with seq[i]
               _permutation(i+1, seq, acc))                             # All permutations that starts with seq[i+1] // This took me so long T-T

    def remove(value, seq):
        if value == seq[0]:
            return seq[1:]
        return (seq[0],) + remove(value, seq[1:])

    return _permutation(0, seq, ())

print(permutation((1, 2, 3)))
print()


# [2] Combination
def combination(seq, k):
    def _combinations(seq, k, comb):
        if k == 0:
            return (comb,)
        if seq == ():
            return ()

        acc = ()
        # Include current
        acc = acc + _combinations(seq[1:], k-1, comb + (seq[0],))
        # Do not include current
        acc = acc + _combinations(seq[1:], k, comb)

        return acc

    return _combinations(seq, k, ())

print(combination((1, 2, 3), 2))
print()


# [3] All Subsequences
def all_subsequences(seq):
    def all_prefix(seq, i):
        if i == 0:
            return ()
        return (seq[:i],) + all_prefix(seq, i-1)
        
    if seq == ():
        return ((),) # () if all non-empty
    return all_prefix(seq, len(seq)) + all_subsequences(seq[1:])

print(all_subsequences((1, 2, 3)))
print()


# [4] Ordered partition
def ordered_partitions(n):
    def _ordered_partitions(n, cur, sums):
        print(f"Call: n={n}, cur={cur}, sums={sums}")

        if n <= 0:
            print(f"  ✅ Base case: returning {sums}")
            return (sums,)
        if cur > n:
            print(f"  ❌ cur={cur} > n={n}, returning empty")
            return ()

        acc = ()
        if n >= cur:
            print(f"➡️ Take {cur} -> new n={n-cur}, reset cur=1, sums={sums+(cur,)}")
            acc = acc + _ordered_partitions(n-cur, 1, sums + (cur,))
        print(f"➡️ Skip {cur} -> keep n={n}, next cur={cur+1}, sums={sums}")
        acc = acc + _ordered_partitions(n, cur+1, sums)

        return acc
    
    return _ordered_partitions(n, 1, ())

print(ordered_partitions(4))
print()


# [5] Unordered partition
def unordered_partitions(n):
    def _unordered_partitions(n, cur):
        if n <= 0:
            return 1
        if cur > n:
            return 0

        return _unordered_partitions(n-cur, cur) + _unordered_partitions(n, cur+1)

    return _unordered_partitions(n, 1)

print(unordered_partitions(4))
print()


# [6] All paths (-|)
def all_paths_a(r, c):
    def _all_paths_a(r, c, acc):
        if r == 0 and c == 0:
            return (acc,)
        
        paths = ()
        if r >= 1:
            paths = paths + _all_paths_a(r-1, c, acc+"-")
        if c >= 1:
            paths = paths + _all_paths_a(r, c-1, acc+"|")
        
        return paths
    
    return _all_paths_a(r, c, "")

print(all_paths_a(2, 2))
print()


# [7] All paths (-|/)
def all_paths_b(r, c):
    def _all_paths_b(r, c, acc):
        if r == 0 and c == 0:
            return (acc,)
        
        paths = ()
        if r >= 1:
            paths = paths + _all_paths_b(r-1, c, acc+"-")
        if c >= 1:
            paths = paths + _all_paths_b(r, c-1, acc+"|")
        if r >= 1 and c >= 1:
            paths = paths + _all_paths_b(r-1, c-1, acc+"/")

        return paths
    
    return _all_paths_b(r, c, "")

print(all_paths_b(2, 2))
print()


# [8] All ab strings
def ab_strings(n):
    def _ab_strings(n, acc): # Add cur here if there's some restrictions, i.e. you can't have more than 3 a's or b's in succession
        if n == 0:
            return (acc,)
        
        ans = ()
        ans = ans + _ab_strings(n-1, acc+'a')
        ans = ans + _ab_strings(n-1, acc+'b')
        return ans

    return _ab_strings(n, "")

print(ab_strings(4))
print()


# [9] Healthy Diet in Prac3l
def healthy_diet(n):
    def _healthy_diet(n, cur, acc):
        if n == 0:
            return (acc,)
        
        ans = ()
        if cur == 'a':
            if n >= 2:
                ans = ans + _healthy_diet(n-2, 't', acc+'aa')
            if n >= 1:
                ans = ans + _healthy_diet(n-1, 't', acc+'a')
        if cur == 't':
            if n >= 1:
                ans = ans + _healthy_diet(n-1, 'a', acc+'t')
            if n >= 2:
                ans = ans + _healthy_diet(n-2, 'a', acc+'tt')

        return ans

    return _healthy_diet(n, 'a', "") + _healthy_diet(n, 't', "")

print(healthy_diet(4))
print()


# [10] Pattern avoiding (no 'ab' allowed from a string consisting of abc)
def ab_avoiding(n):
    def _ab_avoiding(n, cur):
        if n == 0:
            return 1

        acc = 0
        acc = acc + _ab_avoiding(n-1, 'a')
        if cur != 'a':
            acc = acc + _ab_avoiding(n-1, 'b')
        acc = acc + _ab_avoiding(n-1, 'c')

        return acc

    if n == 0:
        return 0
    return _ab_avoiding(n, '')

print(ab_avoiding(3))
print()


# [11] Decomposable
def is_decomposable(n, divisions):
    def _is_decomposable(n, divisions):
        if n == 0:
            return True
        
        return check_all_division(n, 0, divisions)
                
    def check_all_division(n, i, divisions):
        if i >= len(divisions):
            return False
        
        return (n >= divisions[i] and _is_decomposable(n-divisions[i], divisions)) or check_all_division(n, i+1, divisions)

    return _is_decomposable(n, divisions)

print(is_decomposable(5, (2, 4)))
print()


# [12] Parentheticals
def parentheticals(s):
    def find_close(s, acc):
        if s == "":
            return (acc, "")

        # Find closing )
        if s[0] == ")":
            return (acc, s[1:])
        return find_close(s[1:], acc + s[0])

    def _parentheticals(s, acc):
        if s == "":
            return acc

        # Find (
        if s[0] == "(":
            word, rem = find_close(s[1:], "")
            return _parentheticals(rem, acc + (word,))
        return _parentheticals(s[1:], acc)
    
    return _parentheticals(s, ())

print(parentheticals("It's (probably) true. (Can you see why?)"))
print()


# [13] Alice Game
def alice_vs_bob(n):
    def alice_will_win(n):
        if n >= 1 and not bob_will_win(n-1):
            return True
        elif n >= 4 and not bob_will_win(n-4):
            return True

        return False
    
    def bob_will_win(n):
        if n >= 1 and not alice_will_win(n-1):
            return True
        elif n >= 4 and not alice_will_win(n-4):
            return True
        elif n >= 9 and not alice_will_win(n-9):
            return True

        return False
        
    # First move
    if alice_will_win(n):
        return "Alice"
    return "Bob"

print(alice_vs_bob(50))
print()


# [14] Alice Game [Game States]
def alice_vs_bob_states(n):
    def alice_move(n, moves):
        if n <= 0:
            return (("Bob", moves),)

        ending = ()
        if n >= 1:
            ending = ending + bob_move(n-1, (1, *moves))
        if n >= 4:
            ending = ending + bob_move(n-4, (4, *moves))

        return ending
    
    def bob_move(n, moves):
        if n <= 0:
            return (("Alice", moves),)

        ending = ()
        if n >= 1:
            ending = ending + alice_move(n-1, (1, *moves))
        if n >= 4:
            ending = ending + alice_move(n-4, (4, *moves))
        if n >= 9:
            ending = ending + alice_move(n-9, (9, *moves))

        return ending
        
    # First move
    return alice_move(n, ())

print(alice_vs_bob_states(10))
print()

# Thanks for watching ^-^
# Good luck with the HOPE tomorrow mehehehe