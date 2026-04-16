def surprising(L:list[str], other:str) -> list[str]:
    L.append(other.upper())
    return L


words = ["this", "is", "confusing", "code."]
first = surprising(words, "Avoid")
second = surprising(words, "such.")
         # What is the value of words at this point?
         # the value is ["this", "is", "confusing", "code.", "AVOID", "SUCH."]
         # What are the values of first and second at this point?
         # The values are for first = ["this", "is", "confusing", "code.", "AVOID", "SUCH."]
            # and second = ["this", "is", "confusing", "code.", "AVOID", "SUCH."]
         # What happened?
            #The function modified the original list in place so both calls changed the same list and
            # both first and second refer to it.
print()