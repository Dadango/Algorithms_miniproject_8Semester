import tracemalloc
import Kadane as kd
import Divide_and_Conquer as dc
import timeit
from numpy import random as r


def test(inDat):

    # file2write = open("arrays.txt", 'a')
    # file2write.write(inDat.tolist().__str__() + "\n next \n")
    # file2write.close()

    tracemalloc.start()
    dc.findMaxSubArray(inDat, 0, len(inDat)-1)
    print(f"D&C: Peak memory usage was {tracemalloc.get_traced_memory()[1] / 10**6}MB")
    tracemalloc.stop()

    start = timeit.default_timer()
    dc.findMaxSubArray(inDat, 0, len(inDat)-1)
    stop = timeit.default_timer()
    print('D&C: Time: ', stop - start)

    tracemalloc.start()
    kd.findMaxSubArray(inDat)
    print(f"Kadane: Peak memory usage was {tracemalloc.get_traced_memory()[1] / 10**6}MB")
    tracemalloc.stop()

    start = timeit.default_timer()
    kd.findMaxSubArray(inDat)
    stop = timeit.default_timer()
    print('Kadane: Time: ', stop - start)

    return


test(r.randint(-20, 20, size=2000000))
test(r.randint(-20, 20, size=200000))
test(r.randint(30, size=200000))
test(r.randint(-5, 5, size=200000))
test(r.randint(-20, 20, size=1000))

# print(inDat.tolist())
# print(inDat)
