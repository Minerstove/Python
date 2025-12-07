def broken_add(nums, w1, w2):
    if w2 == "even":
        nums_of_w2 = tuple(num for num in nums if num % 2 == 0)

    elif w2 == "odd":
        nums_of_w2 = tuple(num for num in nums if num % 2 != 0)
    
    if w1 == "even":
        if len(nums_of_w2) % 2 == 0:
            return sum(nums) + 1
    elif w1 == "odd":
        if len(nums_of_w2) % 2 != 0:
            return sum(nums) + 1
    
    return sum(nums)

        
assert broken_add((1, 1), "even", "even") == 3, broken_add((1, 1), "even", "even")
assert broken_add((1, 1), "odd", "even") == 2, broken_add((1, 1), "odd", "even")
assert broken_add((2, 1), "odd", "odd") == 4, broken_add((2, 1), "odd", "odd")
assert broken_add((1, 1), "even", "odd") == 3, broken_add((1, 1), "even", "odd")
