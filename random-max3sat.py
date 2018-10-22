from random import randint

k = 5
E = [(1, 2, 3), (-1, 4, 5), (3, 4, -2), (1, 2, -1), (-1, 5, 4)]


# Computes a 7/8 random approximation of max3sat.
# k: The number of variables
# E: List of tuples of variables. Negation of variable is represented by negative value.
# Returns a list for each variable, indicating its assignment.
def max3sat(k, E):
    x = []
    for i in range(1, k+1):
        x.append(randint(0, 1) == 1)
    return x


x = max3sat(k, E)
print(x)
