import typing


def checked_access(L:list[int], idx:int) -> typing.Optional[int]:
    test = idx >= 0 and idx < len(L)    # What is the value of test on each call?
                                            # the first test is first call (idx = 9): False
                                            # the second call is second call (idx = 2): True
    if test:                            # What is this check preventing?
                                            # It prevents an IndexError
        return L[idx]
    else:
        return None


first = checked_access([1, 0, 1], 9)     # What is the value of first? It is none.
second = checked_access([1, 0, 1], 2)    # What is the value of second? It is 1.
print()