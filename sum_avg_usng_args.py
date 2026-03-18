def calc_stats(*args):
    total = 0
    count = 0
    for n in args:
        total += n
        count += 1
    return total, (total / count if count > 0 else 0)
