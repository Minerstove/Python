#put your solution here
#i can't check constraints, so just be honest hehe

#---to test your code, RUN this file---
def level_of_inflation(tup):
    
    def get_rate(num1, num2):
        return num2 - num1
    
    def helper(tup, checker, layer):
        if len(tup) == 2 and tup[0] != tup[1]:
            return "I bite my tongue, it's a bad habit."
        
        enumerated_tup = _enumerate(tup, 1)
        checker = tuple(True if value == tup[0] and len(checker) != 0 else False for value in tup)
        next_tuple = tuple(
            get_rate(tup[i-1], tup[i]) 
            for i, _ in enumerated_tup
            if i < len(tup)
            )
        
        """print(checker)
        print(next_tuple)
        print(layer)"""
        
        if checker and all(checker):
            #print("There is a constant (but not zero) " + ((layer - 1) * "rate of ") + "inflation right now")
            return "There is a constant (but not zero) " + ((layer - 1) * "rate of ") + "inflation right now"
        
        return helper(next_tuple, checker, layer + 1)

    init_checker = (True if value == tup[0] else False for value in tup)
    if all(init_checker):
        return "There is no inflation right now"
    
    return helper(tup, [], 0)
    
def _enumerate(tup, step):
    if len(tup) == 0:
        return ()
    
    return ((step, tup[0]),) + _enumerate(tup[1:], step + 1)

#print(level_of_inflation((2, 4, 6, 8, 10)))
#print(level_of_inflation((1, 4, 9, 16, 25)))

#---to test your code, RUN this file---

if __name__ == "__main__":
    from tester import run_tests
    run_tests()