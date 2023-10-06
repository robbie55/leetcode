def repeatedSubstringPattern(s: str) -> bool:
    length = len(s)

    for i in range(1, int(length/2)+1):
        if length % i == 0:
            numRepeat = int(length / i)
            print(numRepeat)
            subString = s[0:i]
            answer = ""
            for i in range(numRepeat):
                answer += subString
                print(answer)
            if answer == s:
                return True
            
    return False

    
        
        

print(repeatedSubstringPattern("abab"))