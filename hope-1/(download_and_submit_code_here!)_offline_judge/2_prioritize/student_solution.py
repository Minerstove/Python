#put your solution here
#i can't check constraints, so just be honest hehe

#---to test your code, RUN this file---
def prioritize(s):
    
    def helper(parts, index, result):
        if not parts:
            return ()
        if index < 0:
            return result
        if len(parts) == 1:
            return result
        
        if index == 2:
            if parts[0][index] > parts[1][index]:
                return helper(tuple(part[:-1] for part in parts), index - 1, parts[0][0])
            else:
                return helper(tuple(part[:-1] for part in parts), index - 1, parts[1][0])
            
        if index == 1:
            if len(parts[0][0].replace(" ", "")) == len(parts[1][0].replace(" ", "")):

                if parts[0][index] > parts[1][index]:
                    return helper(tuple(part[:-1] for part in parts), index - 1, parts[0][0])
                elif parts[0][index] < parts[1][index]:
                    return helper(tuple(part[:-1] for part in parts), index - 1, parts[1][0])
            
            elif len(parts[0][0].replace(" ", "")) > len(parts[1][0].replace(" ", "")):
                return helper(tuple(part[:-1] for part in parts), index - 1, parts[0][0])
            
            else:
                return helper(tuple(part[:-1] for part in parts), index - 1, parts[1][0])

        elif index == 0:
            if parts[0][index] > parts[1][index]:
                return helper(tuple(part[:-1] for part in parts), index - 1, parts[0][0])
            else:
                return helper(tuple(part[:-1] for part in parts), index - 1, parts[1][0])
    
    print(helper(s, 2, []))
    return helper(s, 2, [])

#sample input: prioritize((("Arm",3,4,5),("Leg",3,50,1)))
#---to test your code, RUN this file---

if __name__ == "__main__":
    from tester import run_tests
    run_tests()