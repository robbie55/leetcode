def isAnagram(s, t):
  if len(s) != len(t): return False

  obj = {}
  for char in s:
    if char not in obj:
      obj[char] = 0
    obj[char] += 1

  for char in t:
    if char not in obj or obj[char] == 0:
      return False
    obj[char] -= 1
  
  return True