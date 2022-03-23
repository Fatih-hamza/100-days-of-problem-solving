# Day 1


# THE PROBLEM:

# today's problem says that we have a number of stairs (n), and we can climb one, two or three stairs each time. we have to create a function
# that takes n as an argument and return the number of ways with which we can climb these n stairs


# THE SOLUTION:

# the idea of this program is the following: the number of ways we have at a stair i is the sum of the number of ways wether we took one stair, two stairs or 
# three stairs at the ith stair. We store calculated values in a memo object (memozation) to calculate them only once (Dynammic Programming)


def stepPerms(n, memo = {1:1, 2:2, 3:4}):
    if n in memo:
        return memo[n]
    elif n < 1:
        return 0
    memo[n] = stepPerms(n-1) + stepPerms(n-2) + stepPerms(n-3)
    return memo[n]


















