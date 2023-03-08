def range(a, b=None, c=None):
    '''
    This function should behave exactly like the built-in range function.
    For example:

    >>> list(range(5))
    [0, 1, 2, 3, 4]
    >>> list(range(1, 5))
    [1, 2, 3, 4]
    >>> list(range(1, 5, 2))
    [1, 3]
    '''

    if b:
        if a < b:
            while a < b:
                if c:
                    if c < 0:
                        return []
                    yield a
                    a += c
                else:
                    yield a
                    a += 1
        elif a > b:
            while a > b:
                if c:
                    if c > 0:
                        return []
                    yield a
                    a += c
                else:
                    return []
    else:
        i = 0
        while i < a:
            yield i
            i += 1
