def sift_down(array, root, size, vis=None):
    """[0, size) 범위에서 root를 내려 보내 최대 힙을 복구합니다."""
    while root * 2 + 1 < size:
        if vis is not None:
            vis.set_root(root)
        child = root * 2 + 1
        right = child + 1
        # 두 자식 중 더 큰 값을 선택합니다.
        if right < size:
            if vis is not None:
                vis.compare(child, right)
            if array[right] > array[child]:
                child = right
        if vis is not None:
            vis.compare(root, child)
        if array[root] >= array[child]:
            break
        if vis is not None:
            vis.swap(root, child)
        array[root], array[child] = array[child], array[root]
        root = child
        if vis is not None:
            vis.draw()


def build_max_heap(array, vis=None):
    # 자식이 있는 마지막 노드부터 루트까지 힙을 만듭니다.
    for root in range(len(array) // 2 - 1, -1, -1):
        sift_down(array, root, len(array), vis)
    if vis is not None:
        vis.set_root()


def Heap_Sort(array, vis=None):
    if vis is not None:
        vis.build_tree()
    build_max_heap(array, vis)
    for end in range(len(array) - 1, 0, -1):
        # 가장 큰 루트를 뒤로 보내고 남은 구간의 힙을 복구합니다.
        if vis is not None:
            vis.swap(0, end)
        array[0], array[end] = array[end], array[0]
        if vis is not None:
            vis.set_tree_size(end)
        sift_down(array, 0, end, vis)
        if vis is not None:
            vis.set_root()
    if vis is not None and array:
        vis.set_tree_size(0)


def main():
    from sort_runner import run_sort
    run_sort(Heap_Sort, "Heap Sort", "elementary_sort.json", "heap")


if __name__ == "__main__":
    main()
