def count_frequencies(array, vis=None):
    """0 이상의 정수마다 등장 횟수를 셉니다."""
    if any(type(value) is not int or value < 0 for value in array):
        raise ValueError("계수 정렬은 0 이상의 정수만 지원합니다.")
    counts = [0] * (max(array, default=-1) + 1)
    for i, value in enumerate(array):
        counts[value] += 1
        if vis is not None:
            vis.step(array, "Count Sort: count frequencies", active=i,
                     counts=counts, bucket=value)
    return counts


def prefix_ends(counts, array=None, vis=None):
    """빈도를 누적합으로 바꿔 각 값의 끝 위치를 구합니다."""
    for value in range(1, len(counts)):
        counts[value] += counts[value - 1]
        if vis is not None:
            vis.step(array, "Count Sort: cumulative end positions",
                     counts=counts, bucket=value)


def place_stably(array, counts, vis=None):
    result = [None] * len(array)
    # 뒤에서부터 배치하면 같은 값의 입력 순서가 유지됩니다.
    for i in range(len(array) - 1, -1, -1):
        value = array[i]
        counts[value] -= 1
        result[counts[value]] = value
        if vis is not None:
            vis.step(array, "Count Sort: stable placement", active=i,
                     counts=counts, bucket=value, result=result,
                     result_index=counts[value])
    return result


def Count_Sort(array, vis=None):
    counts = count_frequencies(array, vis)
    prefix_ends(counts, array, vis)
    array[:] = place_stably(array, counts, vis)
    if vis is not None:
        vis.step(array, "Count Sort: sorted result")


def main():
    from sort_runner import run_sort
    run_sort(Count_Sort, "Count Sort", "count_sort.json", "count")


if __name__ == "__main__":
    main()
