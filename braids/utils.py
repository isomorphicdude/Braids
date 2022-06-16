"""Utilities without weired dependencies."""

def ispermitted(handle):
    """Checks if a handle is permitted."""
    flag = True
    w = handle.word
    j = abs(w[0])
    if j+1 in set(w[1:-1]) and -1*j-1 in set(w[1:-1]):
        flag = False
        # print("Not permitted")
    return flag