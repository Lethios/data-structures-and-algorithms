def selection_sort(arr: list[int]) -> list[int]:
    arr: list[int] = arr.copy()
    n: int = len(arr)

    for i in range(0, n - 1):
        min_idx: int = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

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

    print(selection_sort(arr))
