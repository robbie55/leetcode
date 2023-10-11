
# Lets think about the problem for a second. We are not concerned with the contents
# Of the substring, and we are not
# concerned about the number of each vowels, only whether they are even or odd

# We can't brute force this problem due to the constraints saying the string can be
# 5 * 10^5 in length.

# We can't slididng window this problem either because the only condition we could
# To tell our left side pointer to move would be if that char was a vowel that 
# results in our total for that vowel to be odd;
# we have nothing if that char isn't a vowel

# So, we will choose to use a hashmap / bitmask approach;
# The parity, whether an int is even or odd, is what we need to keep track of;
# This is where we will use a bitmask to represent whether or not a substring meets
# Our parity requirements

# When we initialize our parity, it'll be 0, represented as a bitmask by 00000;
# Each bit will represent the index of a vowel, "aeiou", and the value associated
# With it will represent its parity; 0 = even; 1 = odd

# In order to find our longest string, we will need two pointers, one would be our 
# running sum, our current string, string[0:i], i being the cur index of our loop;
# The other would be behind the running sum, a target in which the shortest substring
# near the beginning in which our parity equals our current parity...
# We will revisit this in depth later

# It's simple math, if you have two substrings in which both have vowels that
# are all even, like a count given as 40006 and 02202,
# where each index represents a vowel,
# and the value associated with that vowel is the number of times it is said in a str,
# subtracting those two would yield a substring with an all
# even number of vowels... 
# 40006 - 02202 = 42204

# Similarly, oddString - oddString = evenString
# 37703 - 15101 = 22602

# In order to see whether or not a substring has a vowel in it, we will need to loop
# through the chars in our given string, we will also need to keep track of the 
# index in order to calculate our length of each stored substring later on

# Using enumerate() and throwing a conditional. if char in "aeiou", we will
# grab the index of the char in our string "aeiou" and flip the corrosponding bit
# from 0 to 1 in our bit mask.

# This now means, if the char was "e" for example, our bit mask would look like 
# 01000 - "aeiou";
# Meaning that at this specific substring up to the index of our current char, 
# the parity of our givenStr[0:i] is odd 

# we dont care if a consonant pops up, we really fucking don't, so nothing happens;
# when a vowel is our current char, our parity bitmask will change, and we will
# store that bitmask along with its current index in our hashmap

# To reiterate how we are finding the longest substring, we need two substrings:
# Our current running sum, the current most index and the length of the string we 
# have parsed so far, if we are at i = 14, our runningsum is string[0:14], the full 
# current length of string in our loop;
# and our target, another substring with index j representing its last character, :j];
# j < i ALWAYS

# in order for this target to be stored, a parity change most occur, if we stay
# the same parity throughout the entire string, then we'd return the entire string

# when the parity does change, we store that change in parity and its index as a KVP
# this key-value pair represents a parity, which determines whether
# or not that substring is even or odd, and it's length, i;
# {parity: i}, 

# If there is parity change resulting in the parity lets say 00100, this represents
# an odd substring, meaning that our current i is the end of an odd substring
# If the parity 00100 has already appeared in our hashmap, we can subtract i,
# the length of our current substring from the value associated with the key in which
# key = current parity, in this case 00100;

# subtracting two odd parity substrings will create an even parity substring

# We will then set out answer to either this most current substring creation resulting
# from the event i described, or keep the answer as the current previos substring 
# creation, depending on which is larger

# Also, we start our hashmap with KVP {0:-1};
# our first parity stored in our hashmap WOULD be 0:0 or someOtherParity:0,
# however this would make it so we would
# never be able to include the first character in our string, since a string's
# max index is i and its length = i+1;
# by adding a KVP with {0:-1}, we are able to include the first char in testcases
# where the first character is apart of our longest subtring;
# parity is 0 since that's what we start at, and technically we are starting at an
# index of the string the does not exist


def longest_substring_with_even_vowels(s):
    dp = {0: -1}
    parity = 0
    answer = 0
    vowels = "aeiou"

    for i, char in enumerate(s):
        if char in vowels:
            index = vowels.index(char)
            parity ^= 1 << index
    
        if parity in dp:
            answer = max(answer, i-dp[parity])
        else:
            dp[parity] = i
    
    
    return answer
      
 

# Example usage:
s1 = "eleetminicoworoep"
print(longest_substring_with_even_vowels(s1))  # Output: 13


