def insert_at(array, end, vis=None):
    """정렬된 앞부분에 array[end]를 끼워 넣습니다."""
    value = array[end]
    i = end - 1
    if vis is not None:
        vis.mark_end(end, pick=True)
    # 같은 값은 이동하지 않으므로 기존 순서가 유지됩니다.
    while i >= 0:
        if vis is not None:
            vis.compare(i, end)
        if array[i] <= value:
            break
        if vis is not None:
            vis.shift(i, i + 1)
        array[i + 1] = array[i]
        i -= 1
    if vis is not None:
        vis.shift(end, i + 1, pick=True)
    array[i + 1] = value
    if vis is not None:
        vis.pick_value = None
        vis.mark_end(end)


def Insertion_Sort(array, vis=None):
    # 첫 원소 하나는 이미 정렬된 구간입니다.
    if vis is not None and array:
        vis.mark_end(0)
    for end in range(1, len(array)):
        insert_at(array, end, vis)


def main():
    from sort_runner import run_sort
    run_sort(Insertion_Sort, "Insertion Sort", "elementary_sort.json", "insertion")


if __name__ == "__main__":
    main()
