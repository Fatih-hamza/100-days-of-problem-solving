# Day 2

# today's problem is the following: Given an array of integers, find the subset of non-adjacent elements with the maximum sum. Calculate the sum of that subset.  

def max_subset(numbers):
    actual_index = 0
    n = len(numbers)
    # base tests
    if n == 0:
        return 0
    elif n <= 3:
        if n == 3:
            return max(numbers[0], numbers[2], numbers[1], numbers[0]+ numbers[2])
        else:
            return max(numbers)
    else:
        # we either pick up the place at the actual index
        potential1 = numbers[actual_index] + max_subset(numbers[actual_index+2:])
        # or we skip this place to have more choice for the rest of the set
        potential2 = max_subset(numbers[actual_index+1:])
        # we return the choice that will maximize the sum  
        return max(potential1, potential2)

# print(plants([9, 1, 3, 9, -19, 1, 1000]))

