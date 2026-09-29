def digit_at(value, divisor):
    """divisor=1은 일의 자리, 10은 십의 자리입니다."""
    return value // divisor % 10


def count_digits(array, divisor):
    counts = [0] * 10
    for value in array:
        counts[digit_at(value, divisor)] += 1
    return counts
