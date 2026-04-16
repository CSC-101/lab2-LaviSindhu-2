def smallest(n:float, m:float) -> float:
    if n < m:
        return n             # For which calls below is this statement evaluated? None of the calls get this to be
                            # evaluated because n is greater or equal to m in both the calls.
    else:
        return m

first = smallest(3, 2)       # What is the value of first? First is 2
second = smallest(2, 2)      # What is the value of second? Is this a reasonable result? Why or why not? The value of
                               # is 2, but this is not a reasonable result because 2 is not less than 2.
print()