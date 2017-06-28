# Deque (DECK) class implementation

# Author: Pradeep K. Pant, ppant@cpan.org

# Problem Statement
# Given a string of opening and closing parentheses, check whether it’s balanced. 
# We have 3 types of parentheses: round brackets: (), square brackets: [], 
# and curly brackets: {}. Assume that the string doesn’t contain any other character 
# than these, no spaces words or numbers. As a reminder, balanced parentheses require 
# every opening parenthesis to be closed in the reverse order opened. For example ‘([])’ 
# is balanced but ‘([)]’ is not. You can assume the input string has no spaces.

# Initialize queue class and set a empty list
def check_parentheses_match(str):
    # first check if thre are even no of parentheses. This is a basic check
    # assuming that there is no space in inout str
    if len(str)%2 != 0:
        return False
    # Set of possible opening brackets
    opening = set('({[')
    # set of Matching tuples
    matches_tuple = set([ ('(',')'), ('[',']'), ('{','}') ]) 
    # Use list as stack if needed one can implement own stack class but here 
    # we'll use empty list to implement stack DS
    stack = []
    # Now we'll check every parentheses in the str. Looping through input str
    for paren in str:
        # Now check if this is in opening bracket list if so append to the list
        if paren in opening:
            stack.append(paren)
        else:
            # check if there are parentheless in stack
            if len(stack)==0:
                return False
            # Check last opened parentheless  First fetch with a pop operation 
            last_opened = stack.pop()
            if (last_opened,paren) not in (matches_tuple):
                return False   
            else:
                return True
                return len(stack)==0
                
# Test
print (check_parentheses_match('([])'))
print (check_parentheses_match('[](){([[[]]])'))