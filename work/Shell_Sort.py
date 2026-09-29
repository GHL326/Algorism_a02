def insert_with_gap(array, end, gap, vis=None):
    """gap만큼 떨어진 원소들 사이에 현재 값을 삽입합니다."""
    value = array[end]
    i = end - gap
    if vis is not None:
        vis.mark_end(end, pick=True)
    while i >= 0:
        if vis is not None:
            vis.compare(i, end)
        if array[i] <= value:
            break
        if vis is not None:
            vis.shift(i, i + gap)
        array[i + gap] = array[i]
        i -= gap
    if vis is not None:
        vis.shift(end, i + gap, pick=True)
    array[i + gap] = value
    if vis is not None:
        vis.pick_value = None
        vis.mark_end(end)


def Shell_Sort(array, vis=None):
    gap = len(array) // 2
    # 간격을 반씩 줄이고 마지막에는 gap=1로 전체를 정렬합니다.
    while gap > 0:
        if vis is not None:
            vis.set_gap(gap)
        for end in range(gap, len(array)):
            insert_with_gap(array, end, gap, vis)
        gap //= 2
    if vis is not None and array:
        vis.mark_end(len(array) - 1)


def main():
    from sort_runner import run_sort
    run_sort(Shell_Sort, "Shell Sort", "elementary_sort.json", "shell")


if __name__ == "__main__":
    main()
