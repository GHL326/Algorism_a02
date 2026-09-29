def find_min_index(array, start):
    """start부터 끝까지 가장 작은 값의 위치를 찾습니다."""
    min_index = start
    for i in range(start + 1, len(array)):
        if array[i] < array[min_index]:
            min_index = i
    return min_index


def Selection_Sort(array):
    # 앞에서부터 최솟값을 하나씩 확정합니다.
    for start in range(len(array)):
        min_index = find_min_index(array, start)
        array[start], array[min_index] = array[min_index], array[start]
