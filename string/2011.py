class Solution:
    """
    Given an array of strings operations containing a list of operations, 
    return the final value of X after performing all the operations.
    """
    def finalValueAfterOperations(self, operations: list[str]) -> int:
     x = 0 
     for i in operations:
         if i == "--X" or i == "X--":
             x -= 1
         elif i == '++X' or i == "X++":
             x += 1
     return x