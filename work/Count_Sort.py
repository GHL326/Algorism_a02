def count_frequencies(array):
    """0 이상의 정수마다 등장 횟수를 셉니다."""
    if any(type(value) is not int or value < 0 for value in array):
        raise ValueError("계수 정렬은 0 이상의 정수만 지원합니다.")
    counts = [0] * (max(array, default=-1) + 1)
    for value in array:
        counts[value] += 1
    return counts


def prefix_ends(counts):
    """빈도를 누적합으로 바꿔 각 값의 끝 위치를 구합니다."""
    for value in range(1, len(counts)):
        counts[value] += counts[value - 1]


def place_stably(array, counts):
    result = [None] * len(array)
    # 뒤에서부터 배치하면 같은 값의 입력 순서가 유지됩니다.
    for i in range(len(array) - 1, -1, -1):
        value = array[i]
        counts[value] -= 1
        result[counts[value]] = value
    return result


def Count_Sort(array):
    counts = count_frequencies(array)
    prefix_ends(counts)
    array[:] = place_stably(array, counts)
