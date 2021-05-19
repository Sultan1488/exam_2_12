def func(*args):
    num_sum = 0
    for i in args:
        try:
            num_sum += i
        except TypeError:
            continue
    return num_sum
