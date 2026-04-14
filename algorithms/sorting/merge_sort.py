def merge(left: list[int], right: list[int]) -> list[int]:
    left_idx: int = 0
    right_idx: int = 0

    merged: list[int] = []

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            merged.append(left[left_idx])
            left_idx += 1
        else:
            merged.append(right[right_idx])
            right_idx += 1

    if left_idx < len(left):
        arr: list[int] = [*merged, *left[left_idx:]]

    if right_idx < len(right):
        arr: list[int] = [*merged, *right[right_idx:]]

    return arr


def merge_sort(arr: list[int]) -> list[int]:
    arr: list[int] = arr.copy()
    n: int = len(arr)

    if n <= 1:
        return arr

    mid: int = n // 2
    left: list[int] = merge_sort(arr[:mid])
    right: list[int] = merge_sort(arr[mid:])

    return merge(left, right)


if __name__ == "__main__":
    arr: list[int] = [
        38,
        27,
        43,
        3,
        9,
        82,
        10,
        1,
        75,
        56,
        14,
        62,
        48,
        91,
        23,
        7,
        55,
        30,
        18,
        99,
    ]

    print(merge_sort(arr))
