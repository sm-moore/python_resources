def append(listt, item):
    return listt.append(item)

def count_to(number):
    """Counts from one to the number provided

    Arguments:
        number {int} -- The number to count to, inclusive

    Returns:
        [list{str}] -- A list of number counts.
    """
    counts = []
    for i in range(number):
        append(counts, f"Number {i+1}")
    return counts