def insertion_sort(arr: list[int]) -> list[int]:
    arr: list[int] = arr.copy()
    n: int = len(arr)

    for i in range(1, n):
        for j in reversed(range(1, i + 1)):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            else:
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

    print(insertion_sort(arr))
