def groupAnagrams(strs):
  hashmap = {}
  answer = []
  for i in strs:
    sortedStr = "".join(sorted(i))
    if sortedStr in hashmap:
      hashmap[sortedStr].append(i)
    else: 
      hashmap[sortedStr] = [i]

  for val in hashmap.values():
    answer.append(val)



  return answer
  
print(groupAnagrams(["abbbbbbbbbbb","aaaaaaaaaaab"]))





# alphabet = "zyxwvutsrqponmlkjihgfedcba"
#   hashmap = {}
#   answers = []
#   for i in strs:
#     bitmask = 0
#     for char in i:
#       charIndex = alphabet.index(char)
#       bitmask ^= 1  << charIndex
#     if bitmask in hashmap:
#       hashmap[bitmask].append(i)
#     else:
#       hashmap[bitmask] = [i]

#   for val in hashmap.values():
#     answers.append(val)
#   return answers

# zyxwvutsrqponmlkjihgfedcba
# abcdefghijklmnopqrstuvwxyz

# SUPER cool solution using bitmask to solve, doesn't pass for some cases tho :(