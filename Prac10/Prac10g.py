def tabulate(headers, data, sep="|", lborder="|", rborder="|"):
    c = len(headers)

    # ---- Print header row ----
    # Join headers with the separator
    header_row = f" {f' {sep} '.join(headers)} "
    print(lborder + header_row + rborder)

    # ---- Compute column widths ----
    # width[i] = max(len(header_i), max length of str(data[row][i]) for each row)
    widths = []
    for i in range(c):
        # get i-th column values: map(get_index(i), data)
        col_values = map(get_index(i), data)
        max_data_len = max(map(len, map(str, col_values)))  # max string length
        widths.append(space_length(headers[i], max_data_len))

    # ---- Print each row ----
    for row in data:
        cells = []
        for i in range(c):
            cells.append(spaces(widths[i], row[i]))
        print(lborder + " " + f" {sep} ".join(cells) + " " + rborder)


# --- helper functions (unchanged) ---

def space_length(header, max_data_length):
    return len(header) if len(header) > max_data_length else max_data_length

def spaces(width, element):
    s = str(element)
    return ' ' * (width - len(s)) + s

def get_index(i):
    def extractor(row):
        return row[i]
    return extractor



tabulate(('n', 'fib(n)', 'factorial(n)'), [
    [0, 0, 1],
    [1, 1, 1],
    [2, 1, 2],
    [3, 2, 6],
    [4, 3, 24],
    [5, 5, 120],
    [6, 8, 720],
    [7, 13, 5040],
    [8, 21, 40320],
    [9, 34, 362880],
    [10, 55, 3628800],
    [11, 89, 39916800],
    [12, 144, 479001600],
    [13, 233, 6227020800],
    [14, 377, 87178291200],
    [15, 610, 1307674368000],
])
