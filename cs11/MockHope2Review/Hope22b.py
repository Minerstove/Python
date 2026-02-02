def partial_cutoffs(input_seq, c):
    window = []
    cutoff_scores = []

    for score in input_seq:
        window.append(score)
        
        if len(window) > c:
            window = sorted(window)
            del window[0]
        #     # print(window)
        # print(f"at {score}, cutoff is {min(window)}")
        cutoff_scores.append(min(window))

    return cutoff_scores
