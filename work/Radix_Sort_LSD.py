import json
from pathlib import Path


DATA_FILE = Path(__file__).parent / "data" / "radix_lsd.json"


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


def Radix_Sort_LSD(array):
    if any(type(value) is not int or value < 0 for value in array):
        raise ValueError("LSD 기수 정렬은 0 이상의 정수만 지원합니다.")
    maximum = max(array, default=0)
    divisor = 1
    # 일의 자리에서 가장 높은 자리까지 순서대로 처리합니다.
    while maximum // divisor > 0:
        sort_digit(array, divisor)
        divisor *= 10


def main():
    data = json.loads(DATA_FILE.read_text(encoding="utf-8-sig"))
    dataset = data["datasets"][0]
    array = dataset["values"][:]
    print("Original array is:", array)
    Radix_Sort_LSD(array)
    print("Sorted array is:", array)


if __name__ == "__main__":
    main()
