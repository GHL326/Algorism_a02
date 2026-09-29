def sift_down(array, root, size):
    """[0, size) 범위에서 root를 내려 보내 최대 힙을 복구합니다."""
    while root * 2 + 1 < size:
        child = root * 2 + 1
        right = child + 1
        # 두 자식 중 더 큰 값을 선택합니다.
        if right < size and array[right] > array[child]:
            child = right
        if array[root] >= array[child]:
            break
        array[root], array[child] = array[child], array[root]
        root = child


def build_max_heap(array):
    # 자식이 있는 마지막 노드부터 루트까지 힙을 만듭니다.
    for root in range(len(array) // 2 - 1, -1, -1):
        sift_down(array, root, len(array))
