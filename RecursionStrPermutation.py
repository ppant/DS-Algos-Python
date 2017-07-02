# List all permutation of a string using recursion

# Author: Pradeep K. Pant, ppant@cpan.org

# Given a string, write a function that uses recursion to output a list of all the possible
# permutations of that string. For example, given s='abc' the function should return
# ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
# Solution strategy: First check for the edge/base case means the case when recursion will be halted. This is
# important otherwise recursion will go further deep ~infinity resulting in segmentation fault.
# some steps:
# 1. Iterate through input string e.g.; abc
# 2. For each character in the input str, set aside the char at that position and get all permutations of the string
# that is left. e.g.; if current iteration is on 'b' then we will try to find all possible combinations with str 'ac'
# 3. Once you have the lits from step 2, add each element from that list to the character from the initial str
# and append to the list of final results so if we are at 'b' then we got the list ['ac', 'ca'], we’d add 'b' to
# those, resulting in 'bac' and 'bca', each of which we’d add to our final results. Return the list of final results.
# We can try other solutions like backtracking for calculating permutations

#  Implement a recursive function for calculating permutations
def permute(str):
    out = []

    # Check for Edge/Base Case
    if len(str) == 1:
        out = [str]

    else:
        # For every letter in string
        for i, let in enumerate(str):

            # For every permutation resulting from Step 2 and 3 described above
            for perm in permute(str[:i] + str[i + 1:]):
                # Add it to output
                out += [let + perm]

    return out
# Test
print(permute('abc'))
# ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

# note: Python has very good library ltertools to do such operations worth to check

