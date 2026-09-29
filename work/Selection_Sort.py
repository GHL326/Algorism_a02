def find_min_index(array, start):
    """start부터 끝까지 가장 작은 값의 위치를 찾습니다."""
    min_index = start
    for i in range(start + 1, len(array)):
        if array[i] < array[min_index]:
            min_index = i
    return min_index
