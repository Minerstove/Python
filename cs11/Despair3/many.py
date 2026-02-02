N = int(input())
items = []
prices = []
means = []
modes = []

counts = {}
current_mode = None
current_mode_count = 0

for i in range(N):
    item, price = input().split()

    items.append(item)
    prices.append(int(price))

    counts[item] = counts.get(item, 0) + 1
    item_count = counts[item]
    if item_count >= current_mode_count:
        current_mode = item
        current_mode_count = item_count

    means.append(sum(prices) / len(prices))
    modes.append(current_mode)

for i in range(N):
    print(means[i])

for i in range(N):
    print(modes[i])

    
    
