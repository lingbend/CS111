import sys

def main(infile, outfile):
    with open(infile, 'r') as file:
        data = file.readlines()
    data = sort(data)
    with open(outfile, 'w') as writefile:
        writefile.writelines(data)


def merge_sorted(left_list, right_list):
    """
    >>> merge_sorted([1,2,3], [9, 13, 14])
    [1, 2, 3, 9, 13, 14]
    >>> merge_sorted([1,2,3,4],[5,6,7,8])
    [1, 2, 3, 4, 5, 6, 7, 8]
    >>> merge_sorted([], [1])
    [1]
    >>> merge_sorted([5], [])
    [5]
    >>> merge_sorted([3, 7, 7, 9], [0, 1, 2])
    [0, 1, 2, 3, 7, 7, 9]
    >>> merge_sorted([2, 14, 29], [1, 3, 3, 15, 94])
    [1, 2, 3, 3, 14, 15, 29, 94]
    """
    merged_list = []
    while len(left_list) > 0 and len(right_list) > 0:
        if left_list[0] > right_list[0]:
            merged_list.append(right_list.pop(0))
        else:
            merged_list.append((left_list.pop(0)))
    merged_list.extend(left_list)
    merged_list.extend(right_list)
    return merged_list

def sort(inlist):
    """
    >>> sort([1,6,9,2,0,-1,66,1])
    [-1, 0, 1, 1, 2, 6, 9, 66]
    >>> sort([1,2,3,4,5,6])
    [1, 2, 3, 4, 5, 6]
    >>> sort([3, 4, 5, 1, 2, 3])
    [1, 2, 3, 3, 4, 5]
    """
    left_list = inlist[:(len(inlist) // 2)]
    right_list = inlist[(len(inlist) // 2):]
    if len(left_list) > 1:
        left_list = sort(left_list)
    if len(right_list) > 1:
        right_list = sort(right_list)
    return merge_sorted(left_list, right_list)

def split_list(inlist):
    left_list = inlist[:(len(inlist) // 2)]
    right_list = inlist[(len(inlist) // 2 + 1):]
    if len(left_list) == 1:
        return left_list
    else:
        split_list(left_list)
    if len(right_list) == 1:
        return right_list
    else:
        split_list(right_list)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])