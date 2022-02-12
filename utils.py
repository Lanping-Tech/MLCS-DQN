
def compare_locations(loc1, loc2):
    """
    Compare two locations.
    """
    dominate = True
    is_dominated = True
    for i in range(len(loc1.index)):
        if loc1.index[i] < loc2.index[i]:
            dominate &= True
            is_dominated &= False
        elif loc1.index[i] > loc2.index[i]:
            dominate &= True
            is_dominated = True
        else:
            dominate &= False
            is_dominated &= True
    if dominate:
        return -1
    elif is_dominated:
        return 1
    else:
        return 0

