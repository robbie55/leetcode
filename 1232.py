def checkStraightLine(coordinates):
  if(len(coordinates) == 1): return False
  


  def getSlope(point, nextPoint):
    [x1, y1] = point
    [x2, y2] = nextPoint
    top = y2 - y1
    bottom = x2 - x1
    print(top, bottom)
    if (top == 0):
      slope = 0
    if (bottom == 0):
      slope = "x"
    else:
      slope = (y2-y1)/(x2-x1)
    return slope
  
  slope = getSlope(coordinates[0], coordinates[-1])
  

  for i in range(len(coordinates)-1):
    curNode = coordinates[i]
    nextNode = coordinates[i+1]
    curSlope = getSlope(curNode, nextNode)
    if (slope != curSlope):
      return False
  return True

print(checkStraightLine([[1,0],[2,0],[3,0],[4,0]]))