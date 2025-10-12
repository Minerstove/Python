def peaks(heights):
    if len(heights) < 3:
        return []
    
    stand_outs = []

    for i in range(1, len(heights) - 1):
        if heights[i - 1] < heights[i] and heights[i + 1] < heights[i]:
            stand_outs.append(i)

    return(stand_outs)
    


assert peaks((2, 5, 5, 1, 2, 1, 3, 1, 9, 10, 8, 3, 9)) == [4, 6, 9], peaks((2, 5, 5, 1, 2, 1, 3, 1, 9, 10, 8, 3, 9))
