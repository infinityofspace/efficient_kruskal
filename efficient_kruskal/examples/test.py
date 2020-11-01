def split(l, left: int, right: int, asc: bool = True) -> int:
    i = left
    piv = l[right]

    for j in range(left, right):
        if (l[j] < piv and asc) or (l[j] > piv and not asc):
            temp = l[i]
            l[i] = l[j]
            l[j] = temp
            i += 1

    temp = l[i]
    l[i] = l[right]
    l[right] = temp

    return i


def quick_sort(l, left: int = None, right: int = None, asc: bool = True):
    if left is None:
        left = 0

    if right is None:
        right = len(l) - 1

    if len(l) == 1:
        return l

    if left < right:
        split_idx = split(l, left, right, asc)
        quick_sort(l, left, split_idx - 1)
        quick_sort(l, split_idx + 1, right)


if __name__ == '__main__':
    a = [5, 4, 8, 6, 4, 5, 3, 1]
    quick_sort(a, asc=False)
    print(a)
