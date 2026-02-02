def _enumerate(s,i):
    if len(s) == 0:
        return ()
    return ((i, s[0]),) + _enumerate(s[1:], i + 1)
#print(_enumerate((213, 2143, 213), 1))

def _max(nums):
    if len(nums) == 1:
        return nums[0]
    
    if nums[0] >= nums[1]:
        return _max((nums[0],) + nums[2:])
    else:
        return _max(nums[1:])
#print(_max((213, 2143234, 213213)))

def _min(nums):
    if len(nums) == 1:
        return nums[0]
    
    if nums[0] <= nums[1]:
        return _min((nums[0],) + nums[2:])
    else:
        return _min(nums[1:])
#print(_min((213, 2121312343, 213213)))

def _sum(nums):
    if len(nums) == 0:
        return 0
    
    return nums[0] + _sum(nums[1:])
#print(_sum((213, 2121312343, 213213)))

def _sorted(nums):
    def helper():
        ...
    
    return helper()
#print(_sorted((213, 2121312343, 213213)))

def _any(tup):
    ...

def _all(tup):
    if not tup[0]:
        return False
    if len(tup) == 1:
        return tup[0]
    
    return _all(tup[1:])
print(_all((True, False, True, True, False)))

def _zip(tup1, tup2):
    ...
    
def _flipgrid(grid):
    ...

def _range(num1, num2):
    ...
