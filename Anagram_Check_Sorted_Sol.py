# Anagram Check - Easy and direct solution using sort
# Author: Pradeep K. Pant, ppant@cpan.org

# if two strings have the same frequency of letters/element (meaning each letter shows up the same number of times in both strings)
# then they are anagrams of each other. On a similar logic, if two strings are equal to each other once they are sorted,
# then they are also anagrams of each other.

def anagram(str1,str2):
    # First we'll remove white spaces and also convert string to lower case letters
    str1 = str1.replace(' ','').lower()
    str2 = str2.replace(' ','').lower()
     # We'll show output in the form of boolean TRUE/FALSE for the sorted match hence return 
    return sorted(str1) == sorted(str2)

#  Test
#Some examples of anagram:
#	"dormitory" is an anagram of "dirty room"
#	"a perfectionist" is an anagram of "I often practice."
#	"action man" is an anagram of "cannot aim"

result = anagram('dormitory','dirty room')
print (result);
