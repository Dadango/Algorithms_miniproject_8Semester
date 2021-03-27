import sys


def findMaxCrossingSubArrSum(arrayIn, low, mid, high):
    leftSum = - sys.maxsize  # - alot to be safe
    sm = 0

    for i in range(mid, low - 1, -1):  # go from mid to low (left)
        sm += arrayIn[i]  # add element to sum

        if sm > leftSum:  # set leftsum to highest sum
            leftSum = sm

    rightSum = - sys.maxsize  # same as with left, but right
    sm = 0

    for i in range(mid + 1, high + 1):
        sm = sm + arrayIn[i]

        if sm > rightSum:
            rightSum = sm

    # return sum of elements on left and right of mid (or either if that's larger, such as for [-2, 1])
    return max(leftSum + rightSum, leftSum, rightSum)


def findMaxSubArray(arrayIn, low, high):
    if high == low:  # best case: only 1 element
        return arrayIn[low]
    mid = (low+high)//2  # floor division to find middle point
    maxLeft = findMaxSubArray(arrayIn, low, mid)  # max subarray in right half
    maxRight = findMaxSubArray(arrayIn, mid + 1, high)  # max subarray in right half
    maxCrossing = findMaxCrossingSubArrSum(arrayIn, low, mid, high)  # max subarray that crosses midpoint
    return max(maxLeft, maxRight, maxCrossing)  # get largest sum of the 3


'''
inDat = [9, -6, -12, -2, 10, 0, -7, 14, -5, 2, 12, -13, -3, -8, 4, -9, 3, 11, -10, 7]
result = findMaxSubArray(inDat, 0, len(inDat)-1)
print("largest sum was: " + result.__str__())
'''

# complexity is: O(n log n)
# O(1) space required
