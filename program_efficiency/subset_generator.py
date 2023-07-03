def genSubsets(L):
    """Generating all sub-sets
    """
    if len(L) == 0:
        return [[]]  # list of empty list
    smaller = genSubsets(L[:-1])  # all subsets without last element
    extra = L[-1:]  # create a list of just last element
    new = []
    for small in smaller:
        # for all smaller solutions, add one with last element
        new.append(small+extra)
    return smaller+new  # combine those with last element and those without


testSet = [1, 2, 3, 4]
print(genSubsets(testSet))
