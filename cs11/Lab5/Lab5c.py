def num_subarrays(a, p):
    a2 = get_subarrays(a)
    result = 0

    for subarray in a2:
        product = 1
        for element in subarray:
            product *= element
        if product <= p:
            result += 1
    
    return result


def get_subarrays(arr):
    n = len(arr)
    subarrays = []
    for i in range(n):
        for j in range(i, n):
            subarrays.append(arr[i:j+1])
    return subarrays

assert num_subarrays((2, 1, 2), 3) == 5, num_subarrays((2, 1, 2), 3)

