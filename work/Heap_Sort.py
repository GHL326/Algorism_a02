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
