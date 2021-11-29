import math
import numpy as np

# PURPOSE: Returns an array representing each rank of each number in given array
def ordArr(arr):
    arr = np.array(arr)
    order = arr.argsort()
    ranks = order.argsort() + 1
    return ranks

def wilcoxon(arr, mean):
    table = []
    yi = []
    abs_yi = []
    rank = []
    signed_rank = []

    # yi row
    for num in arr:
        yi.append(num-mean)
    table.append(yi)

    #abs_yi
    for num in yi:
        abs_yi.append(abs(num))
    table.append(abs_yi)

    # rank
    rank = ordArr(abs_yi)
    table.append(rank)

    # signed_rank
    count = 0
    for num in yi:
        if num < 0:
            signed_rank.append(0 - rank[count])
        else:
            signed_rank.append(rank[count])
        count += 1
    table.append(signed_rank)

    # test statistic
    test_stat = 0 # Placeholder
    for num in signed_rank:
        if num > 0:
            test_stat += num
    print(test_stat)

    return table, test_stat

if __name__ == "__main__":
    arr = [745.5, 1175.0, 1290.0, 1364.5, 1397.5, 1660.0]
    mean = 1386

    results = wilcoxon(arr, mean)
    print(np.matrix(results))