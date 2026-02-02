#put your solution here
#i can't check constraints, so just be honest hehe

#---to test your code, RUN this file---
def prioritize(s):

    def recursive_helper(input):
        if len(input) == 1:
            return input[0][0]
        
        winner_name = helper((input[0], input[1]), 2, None)
        winner_tuple = input[0] if input[0][0] == winner_name else input[1]
        
        return recursive_helper((winner_tuple,) + input[2:])

    def helper(parts, index, result):
        if not parts:
            return ()
        # base: if all rules tied, use ID; otherwise return the earlier winner
        if index < 0:
            return result if result is not None else (
                parts[0][0] if parts[0][3] > parts[1][3] else parts[1][0]
            )
        if len(parts) == 1:
            return result
        
        if index == 2:  # distance (smaller wins) -> tuple field 1
            if parts[0][1] < parts[1][1]:
                return parts[0][0]                 # immediate return
            elif parts[0][1] > parts[1][1]:
                return parts[1][0]                 # immediate return
            else:  # tie -> next rule
                return helper(parts, index - 1, result)
            
        if index == 1:  # fragility (higher wins) -> tuple field 2
            if parts[0][2] > parts[1][2]:
                return parts[0][0]                 # immediate return
            elif parts[0][2] < parts[1][2]:
                return parts[1][0]                 # immediate return
            else:  # tie -> next rule
                return helper(parts, index - 1, result)

        elif index == 0:  # name length (ignoring spaces; shorter wins) -> tuple field 0
            l0 = len(parts[0][0].replace(" ", ""))
            l1 = len(parts[1][0].replace(" ", ""))
            if l0 < l1:
                return parts[0][0]                 # immediate return
            elif l1 < l0:
                return parts[1][0]                 # immediate return
            else:  # tie -> next rule (ID handled in base case)
                return helper(parts, index - 1, result)

    return recursive_helper(s)

#sample input: prioritize((("Arm",3,4,5),("Leg",3,50,1)))
#---to test your code, RUN this file---

if __name__ == "__main__":
    from tester import run_tests
    run_tests()