k = 5
E = [(1, 2, 3), (-1, 4, 5), (3, 4, -2), (1, 2, -1), (-1, 5, 4)]


# Computes a 7/8 deterministic approximation of max3sat.
# k: The number of variables
# E: List of tuples of variables. Negation of variable is represented by negative value.
# Returns a list for each variable, indicating its assignment.
def max3sat(k, E):
    x = []
    for i in range(1, k+1):
        expectationIfTrue = expectation(i, E)
        expectationIfFalse = expectation(-i, E)
        assignTrue = expectationIfTrue > expectationIfFalse
        x.append(assignTrue)
        if assignTrue:
            E = prune(i, E)
        else:
            E = prune(-i, E)

    return x


# Calculates the expectation for the number of satisfied clauses, assuming a particular variable is true.
# v: Variable assumed to be true.
# E: List of tuples of variables. Negation of variable is represented by negative value.
# Returns the expectation as a floating point number.
def expectation(v, E):
    e = 0
    for c in E:
        if v in c:
            e = e + 1
        else:
            numVars = len(c)
            numNotV = c.count(-v)
            e = e + 1 - 2**-(numVars-numNotV)

    return e


# Computes a new list of tuples, leftover from assuming that a particular variable is true.
# v: Variable assumed to be true.
# E: List of tuples of variables. Negation of variable is represented by negative value.
# Returns a new list of tuples.
def prune(v, E):
    newE = []
    for c in E:
        if v in c or len(c) == 0:
            continue

        newC = tuple((a for a in c if a != -v))
        newE.append(newC)

    return newE


x = max3sat(k, E)
print(x)
