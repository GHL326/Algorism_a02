def find_min_index(array, start, vis=None):
    """start부터 끝까지 가장 작은 값의 위치를 찾습니다."""
    min_index = start
    if vis is not None:
        vis.selection(min_index)
    for i in range(start + 1, len(array)):
        if vis is not None:
            vis.compare(i, min_index)
        if array[i] < array[min_index]:
            min_index = i
            if vis is not None:
                vis.selection(min_index)
                vis.draw()
                vis.wait(500)
    return min_index


def Selection_Sort(array, vis=None):
    # 앞에서부터 최솟값을 하나씩 확정합니다.
    for start in range(len(array)):
        min_index = find_min_index(array, start, vis)
        if start != min_index:
            if vis is not None:
                vis.swap(start, min_index)
            array[start], array[min_index] = array[min_index], array[start]
        if vis is not None:
            vis.mark_done(start)


def main():
    from sort_runner import run_sort
    run_sort(Selection_Sort, "Selection Sort", "elementary_sort.json", "selection")


if __name__ == "__main__":
    main()
