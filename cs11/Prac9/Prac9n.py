def kris_kringle_k(k, ntuple):
    # Build mapping of recipient → gifter
    recipient_to_gifter = {recipient: gifter for gifter, recipient, _ in ntuple}
    # Map gifter → their original gift
    gift_of = {gifter: gift for gifter, _, gift in ntuple}

    result = {}
    visited = set()

    for person in recipient_to_gifter:
        if person in visited:
            continue

        # Step 1: Find the cycle this person belongs to
        cycle = []
        curr = person
        while curr not in visited:
            visited.add(curr)
            cycle.append(curr)
            curr = recipient_to_gifter[curr]

        # Step 2: Apply k modulo cycle length
        L = len(cycle)
        shift = k % L

        # Step 3: Assign final gifts for this whole cycle
        for i, recipient in enumerate(cycle):
            # Gift comes from person shift steps upstream
            gifter = cycle[(i + shift) % L]
            result[recipient] = gift_of[gifter]

    # Step 4: Return alphabetically sorted dict
    return dict(sorted(result.items()))




assert kris_kringle_k(5, (
    ('Rufus', 'Rufus', 'Pistol'),
    ('Reno', 'Rude', 'Glasses'),
    ('Rude', 'Tseng', 'Shades'),
    ('Tseng', 'Reno', 'Glasses'),
    ('Elena', 'Cissnei', 'Materia'),
    ('Cissnei', 'Elena', 'Glasses'),
)) == {
    'Cissnei': 'Materia',
    'Elena': 'Glasses',
    'Rufus': 'Pistol',
    'Reno': 'Shades',
    'Rude': 'Glasses',
    'Tseng': 'Glasses',
}, kris_kringle_k(5, (
    ('Rufus', 'Rufus', 'Pistol'),
    ('Reno', 'Rude', 'Glasses'),
    ('Rude', 'Tseng', 'Shades'),
    ('Tseng', 'Reno', 'Glasses'),
    ('Elena', 'Cissnei', 'Materia'),
    ('Cissnei', 'Elena', 'Glasses'),
))

        