import math

def diagonalSum(mat):
    sum = 0
    middle = None
    rowLength = len(mat[0])
    if (len(mat) % 2 !=0 and rowLength %2 !=0):
      middle = math.floor((len(mat)/2))
      print(middle)
    for i in range(len(mat)):
      front = mat[i]
      print(front)
      frontVal = front[i]
      backVal = front[-i -1]
      print(frontVal, backVal)
      if (len(mat) == 1):
        if (len(front) == 1):
          sum += frontVal
          return sum
        sum +=  frontVal + backVal 
      if (i == middle):
         sum+=frontVal
      else:
         sum+=frontVal    
         sum+=backVal  
        
    return sum
             
             

print(diagonalSum([[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]))