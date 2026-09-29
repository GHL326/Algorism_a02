def insert_with_gap(array, end, gap):
    """gap만큼 떨어진 원소들 사이에 현재 값을 삽입합니다."""
    value = array[end]
    i = end - gap
    while i >= 0 and array[i] > value:
        array[i + gap] = array[i]
        i -= gap
    array[i + gap] = value
