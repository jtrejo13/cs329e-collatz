#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2017
# Juan Trejo
# ---------------------------

# ------------
# collatz_read
# ------------

def collatz_read(s):
    """
    read two ints
    s a string
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    a = s.split()
    return [int(a[0]), int(a[1])]

# ------------
# collatz_eval
# ------------

def collatz_eval(i, j):
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """
    assert(i > 0 and j > 0)
    max_cycle = 1
    for n in range(i, j + 1):
        cycle = collatz_cycle(n)
        if cycle > max_cycle:
            max_cycle = cycle
    assert(max_cycle > 0)
    return max_cycle

# ------------
# collatz_cycle (helper)
# ------------

def collatz_cycle(n):
    """
        compute collatz cycle length
        n int to be computed
        return the cycle length of n
    """
    assert(n > 0)
    cycle_length = 1
    while n > 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = 3 * n + 1
        cycle_length += 1
    assert(cycle_length > 0)
    return cycle_length

# -------------
# collatz_print
# -------------

def collatz_print(w, i, j, v):
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve(r, w):
    """
    r a reader
    w a writer
    """
    for s in r:
        i, j = collatz_read(s)
        v = collatz_eval(i, j)
        collatz_print(w, i, j, v)
