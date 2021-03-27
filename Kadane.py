import sys
import random


def findMaxSubArray(arrayIn):
    best_sum = -sys.maxsize
    current_sum = 0
    for x in arrayIn:
        current_sum = max(0, current_sum + x)
        best_sum = max(best_sum, current_sum)
    return best_sum


def maxSubarray(arrayIn):
    """Find a contiguous subarray with the largest sum."""
    best_sum = -sys.maxsize
    best_start = best_end = 0
    current_sum = current_start = 0
    for current_end, x in enumerate(arrayIn):
        if current_sum <= 0:
            # Start a new sequence at the current element
            current_start = current_end
            current_sum = x
        else:
            # Extend the existing sequence with the current element
            current_sum += x

        if current_sum > best_sum:
            best_sum = current_sum
            best_start = current_start
            best_end = current_end + 1  # the +1 is to make 'best_end' exclusive

    return best_sum, best_start, best_end


'''
inDat = [9, -6, -12, -2, 10, 0, -7, 14, -5, 2, 12, -13, -3, -8, 4, -9, 3, 11, -10, 7]
print(inDat)
result = findMaxSubArray(inDat)
print(maxSubarray(inDat))
print("largest sum was: " + result.__str__())
'''
# complexity is O(n)
# O(1) space required
