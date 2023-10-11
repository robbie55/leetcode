# def canIWin(maxChoosableInteger, desiredTotal):
#   choices = list(range(maxChoosableInteger, -1, -1))
#   choicesUsed = 0
#   total = 0
#   skipped = 0
#   print(choices)
#   for i, val in enumerate(choices):

#     if val + total <= desiredTotal:
#       total += val
#       choiceIndex = choices.index(val)
#       choicesUsed ^= 1 << choiceIndex
#     else:
#       skipped += 1

#     if total == desiredTotal:
#       check = (i - skipped)
#       if check % 2 == 1:
#         return True
#       return False

    



#   return

def canIWin(maxChoosableInteger: int, desiredTotal: int) -> bool:
    if (1 + maxChoosableInteger) * maxChoosableInteger // 2 < desiredTotal:
        return False

    memo = {}

    def can_win(used, remaining):
        if used in memo:
            return memo[used]

        for i in range(1, maxChoosableInteger + 1):
            mask = 1 << (i - 1)
            if used & mask == 0:
                if i >= remaining or not can_win(used | mask, remaining - i):
                    memo[used] = True
                    return True

        memo[used] = False
        return False

    return can_win(0, desiredTotal)

# Example usage:

print(canIWin(10, 40))