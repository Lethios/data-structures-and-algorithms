def bubble_sort(arr: list[int]) -> list[int]:
    arr: list[int] = arr.copy()
    n: int = len(arr)

    for i in reversed(range(0, n)):
        swapped = False

        for j in range(0, i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

    return arr


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

    print(bubble_sort(arr))
