def sum_pairs(lst, s):  # O(n), don't use indexes!
    cache = set()
    for i in lst:
        if s - i in cache:
            return [s - i, i]
        cache.add(i)