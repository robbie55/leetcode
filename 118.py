def generate(numRows: int):
    answer = [[1]]
    if numRows == 1:
        return answer
    for row in range(numRows-1):
        prevRow = answer[row]
        newRow = [0]
        print(prevRow)
        for prevListIndex in range(len(prevRow)):
            newRow.append(0)
            newRow[prevListIndex] += prevRow[prevListIndex]
            newRow[prevListIndex+1] += prevRow[prevListIndex]
        answer.append(newRow)
    return answer


print(generate(5))
