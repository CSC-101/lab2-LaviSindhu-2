def function2(a:int, b:int, c:int) -> int:
    if a > b and a > c:
        return a - b             # In general, when will a call to this function evaluate this statement?
    elif b > c:                     # Only when A is the largest Value.
        return b + c             # In general, when will a call to this function evaluate this statement?
    else:                           # If b is greater than c.
        return 2 * c             # In general, when will a call to this function evaluate this statement?
                                        #If A is not the largest valur and if b is smaller than c.

answer1 = function2(3, 2, 1)     # What is the value of answer1? the value is 1
answer2 = function2(2, 3, 1)     # What is the value of answer2? the value is 4
answer3 = function2(2, 1, 3)     # What is the value of answer3? the value is 6
print()