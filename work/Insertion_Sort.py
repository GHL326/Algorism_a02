def insert_at(array, end):
    """정렬된 앞부분에 array[end]를 끼워 넣습니다."""
    value = array[end]
    i = end - 1
    # 같은 값은 이동하지 않으므로 기존 순서가 유지됩니다.
    while i >= 0 and array[i] > value:
        array[i + 1] = array[i]
        i -= 1
    array[i + 1] = value


def Insertion_Sort(array):
    # 첫 원소 하나는 이미 정렬된 구간입니다.
    for end in range(1, len(array)):
        insert_at(array, end)
