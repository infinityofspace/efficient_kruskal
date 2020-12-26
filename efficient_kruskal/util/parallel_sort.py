import math
import random
import time
from multiprocessing import Pool, cpu_count


def merge(l, r):
    sorted_list = []
    l_idx = 0
    r_idx = 0

    while l_idx < len(l) and r_idx < len(r):
        if l[l_idx] <= r[r_idx]:
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


def merge_sort(data):
    if len(data) <= 1:
        return data

    split_idx = int(len(data) / 2)

    l = merge_sort(data[:split_idx])
    r = merge_sort(data[split_idx:])

    return merge(l, r)


def parallel_mergesort(data):
    pool = Pool(processes=cpu_count())

    chunk_size = math.ceil(len(data) / cpu_count())

    chunked_data = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]

    sorted_parts = pool.map(merge_sort, chunked_data)

    while len(sorted_parts) > 1:
        i = iter(sorted_parts)
        tuple_list = list(zip(i, i))
        if len(sorted_parts) % 2 == 0:
            sorted_parts = pool.starmap(merge, tuple_list)
        else:
            sorted_parts = pool.starmap(merge, tuple_list) + sorted_parts[-1:]

    return sorted_parts[0]


if __name__ == '__main__':
    size = 100000

    data_unsorted = [random.randint(0, size) for _ in range(size)]
    a = time.time()
    sorted_data = parallel_mergesort(data_unsorted)
    print(time.time() - a)

    print(data_unsorted == sorted_data)