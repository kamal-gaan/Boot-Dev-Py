# COMPARISON OPERATOR EVALUATIONS
# When a comparison happens, the result of the comparison is just a boolean value, it's either True or False.

# Take the following two examples:

# is_bigger = 5 > 4
# Copy icon
# is_bigger = True
# Copy icon
# In both of the above cases, we're creating a Boolean variable called is_bigger with a value of True.

# Because 5 is greater than 4, is_bigger is assigned the value of True.

# ASSIGNMENT
# Create the following variables. Use comparison operators to determine their boolean values. The context of the parameter names should tell you how to make these comparisons. Return them in this order:

# is_mustang_edward_same
# is_alphonse_edward_same
# is_winry_alphonse_same

def compare_heights(edward_height, alphonse_height, winry_height, mustang_height):
    is_mustang_edward_same = mustang_height == edward_height
    is_alphonse_edward_same = alphonse_height == edward_height
    is_winry_alphonse_same = winry_height == alphonse_height

    return is_mustang_edward_same, is_alphonse_edward_same, is_winry_alphonse_same
    pass
