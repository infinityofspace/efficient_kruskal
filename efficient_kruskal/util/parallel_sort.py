import math
from multiprocessing import Pool, cpu_count
from typing import List


def merge(l: List, r: List) -> List:
    """
    Merge and sort two list parts in ascending order.

    :param l: left part of the list
    :param r: right part of the list
    :return: merged and sorted list of r and l
    """

    sorted_list = []
    l_idx = 0
    r_idx = 0

    while l_idx < len(l) and r_idx < len(r):
        if l[l_idx][2] <= r[r_idx][2]:
            sorted_list.append(l[l_idx])
            l_idx += 1
        else:
            sorted_list.append(r[r_idx])
            r_idx += 1

    if l_idx < len(l):
        sorted_list.extend(l[l_idx:])
    elif r_idx < len(r):
        sorted_list.extend(r[r_idx:])

    return sorted_list


def mergesort(data: List) -> List:
    """
    Recursive split the provided list into nearly equal sized left and right part and sort them in ascending order.
    The used algorithm is mergesort.

    :param data: list of data to be sorted
    :return: sorted list
    """

    if len(data) <= 1:
        return data

    split_idx = int(len(data) / 2)

    l = mergesort(data[:split_idx])
    r = mergesort(data[split_idx:])

    return merge(l, r)


def parallel_mergesort(data: List) -> List:
    """
    Sort the provided list in ascending order with parallel mergesort algorithm.

    :param data: list of data to be sorted
    :return: sorted list
    """

    pool = Pool(processes=cpu_count())

    chunk_size = math.ceil(len(data) / cpu_count())

    chunked_data = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]

    sorted_parts = pool.map(mergesort, chunked_data)

    while len(sorted_parts) > 1:
        i = iter(sorted_parts)
        tuple_list = list(zip(i, i))
        if len(sorted_parts) % 2 == 0:
            sorted_parts = pool.starmap(merge, tuple_list)
        else:
            sorted_parts = pool.starmap(merge, tuple_list) + sorted_parts[-1:]

    return sorted_parts[0]
