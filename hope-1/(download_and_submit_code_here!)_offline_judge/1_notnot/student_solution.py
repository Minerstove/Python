#put your solution here
#i can't check constraints, so just be honest hehe
#---to test your code, RUN this file---

def notnot(s):
    def only_nots(words):
        if len(words[:-1]) % 2 == 0:
            return "not"
        else:
            return "not not"

    def helper(words, result):
        if not words:
            return result
        
        word = words[0]
        rest = words[1:]
        
        if word.lower() == "not":
            if result and result[-1].lower() == "not":
                return helper(rest, result[:-1])
            else:
                return helper(rest, result + [word.lower()])
        else:
            return helper(rest, result + [word.lower()])

    if len(s.split(" ")) == len([word for word in s.split(" ") if word.lower() == "not"]):
        return only_nots(s.split(" "))
    else:
        return " ".join(helper(s.split(" "), []))
    
#---to test your code, RUN this file---

if __name__ == "__main__":
    from tester import run_tests
    run_tests()