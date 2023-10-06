from collections import defaultdict

def equalPairs(grid):

        counter = defaultdict(int)
        # Creating a dictionary to store out individual rows in, defaulty
        # assigning a number, 0, for each value

        for row in grid:
            counter[tuple(row)] += 1
            # each row is assigned a value of 1, while also being turned into a tuple
            # We see the reason for this later


        res = 0
        # Setting our counter to 0

        for col in zip(*grid):
            # out zip function "zips" together two arguments into lists
            # the "*" before our grid unpacks our grid list into seperate rows
            # zip only works on tuples, and grabs the first index of each argument
            # and creates a new list for those values, creating columns


            res += counter[tuple(col)]
            # Here we check to see if the columns we have, turned tuples, are a key
            # in our dictionary. defaultdict will return 0 if the key DNE,
            # since our keys are our rows from the grid, if the column == row,
            # it will have the value "1" assigned to it


        return res



  # count = 0

  # def rowsToColumns(rows):
  #   columnGrid = []
  #   curColumn = []
  #   for i in range(len(rows)):
  #     for row in grid:
  #       curColumn.append(row[i])
  #     columnGrid.append(curColumn)
  #     curColumn = []
  #   return columnGrid

  # columnGrid = rowsToColumns(grid)

  # for row in grid:
  #   for column in columnGrid:
  #     if row == column:
  #       count += 1

  # return count

print(equalPairs([[3,2,1],[1,7,6],[2,7,7]]))