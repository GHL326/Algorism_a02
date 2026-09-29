def count_frequencies(array):
    """0 이상의 정수마다 등장 횟수를 셉니다."""
    if any(type(value) is not int or value < 0 for value in array):
        raise ValueError("계수 정렬은 0 이상의 정수만 지원합니다.")
    counts = [0] * (max(array, default=-1) + 1)
    for value in array:
        counts[value] += 1
    return counts
