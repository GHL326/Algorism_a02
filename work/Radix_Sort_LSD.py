def digit_at(value, divisor):
    """divisor=1은 일의 자리, 10은 십의 자리입니다."""
    return value // divisor % 10


def count_digits(array, divisor):
    counts = [0] * 10
    for value in array:
        counts[digit_at(value, divisor)] += 1
    return counts


def sort_digit(array, divisor):
    counts = count_digits(array, divisor)
    for digit in range(1, 10):
        counts[digit] += counts[digit - 1]

    result = [None] * len(array)
    # 현재 자리 숫자가 같으면 이전 자리 정렬 순서를 유지합니다.
    for i in range(len(array) - 1, -1, -1):
        digit = digit_at(array[i], divisor)
        counts[digit] -= 1
        result[counts[digit]] = array[i]
    array[:] = result
