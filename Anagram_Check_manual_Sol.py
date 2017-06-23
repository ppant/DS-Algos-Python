# Anagram Check - Mnual solution using counting and hash tables 
# Author: Pradeep K. Pant, ppant@cpan.org

# if two strings have the same frequency of letters/element 
# (meaning each letter shows up the same number of times in both strings)
# then they are anagrams of each other. 
# In manual solution we'll count the number of letters in each string 
# this will help in understanding hash tables so the solution will 
# use couting with Python dictionaries:

def anagram(str1,str2):
    # First we'll remove white spaces and also convert string to lower case letters
    str1 = str1.replace(' ','').lower()
    str2 = str2.replace(' ','').lower()
    
      
    # Edge Case to check if same number of letters
    if len(str1) != len(str2):
        return False
    
    # Manually create counting dictionary 
    # Logic is to check each letter in the first string and increse the count
    # and in second string we loop throughh and then check for the each letter 
    # in count dictionary and if found and decrese the count 
    # finally we check if count is Zero which means that we found anagram
    # Initilize dictionary
    count = {} 
        
    # Fill dictionary for first string (add counts)
    for letter in str1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
            
    # Fill dictionary for second string (subtract counts)
    for letter in str2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1
    
    # Check that all counts are 0
    for k in count:
        if count[k] != 0:
            return False

    # Otherwise they're anagrams
    return True
     # We'll show output in the form of boolean TRUE/FALSE for the sorted match hence return 
   
#  Test
#Some examples of anagram:
#	"dormitory" is an anagram of "dirty room"
#	"a perfectionist" is an anagram of "I often practice."
#	"action man" is an anagram of "cannot aim"

result = anagram('dormitory','dirty room')
print (result);
