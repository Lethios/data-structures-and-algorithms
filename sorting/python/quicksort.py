from random import randint


def quicksort(arr: list[int]) -> list[int]:
    arr: list[int] = arr.copy()
    n: int = len(arr)

    if n <= 1:
        return arr

    pivot_idx: int = randint(0, n - 1)
    arr[pivot_idx], arr[-1] = arr[-1], arr[pivot_idx]
    pivot_idx: int = n - 1

    i: int = -1
    for j in range(n - 1):
        if arr[j] < arr[pivot_idx]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[-1] = arr[-1], arr[i + 1]

    left: list[int] = arr[: i + 1]
    right: list[int] = arr[i + 2 :]

    return [*quicksort(left), arr[i + 1], *quicksort(right)]


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

    print(quicksort(arr))
