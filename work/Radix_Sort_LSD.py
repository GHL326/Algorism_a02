def digit_at(value, divisor):
    """divisor=1은 일의 자리, 10은 십의 자리입니다."""
    return value // divisor % 10


def count_digits(array, divisor, vis=None):
    counts = [0] * 10
    for i, value in enumerate(array):
        digit = digit_at(value, divisor)
        counts[digit] += 1
        if vis is not None:
            vis.step(array, f"LSD: divisor={divisor}, count digits", active=i,
                     counts=counts, bucket=digit)
    return counts


def sort_digit(array, divisor, vis=None):
    counts = count_digits(array, divisor, vis)
    for digit in range(1, 10):
        counts[digit] += counts[digit - 1]
        if vis is not None:
            vis.step(array, f"LSD: divisor={divisor}, cumulative positions",
                     counts=counts, bucket=digit)

    result = [None] * len(array)
    # 현재 자리 숫자가 같으면 이전 자리 정렬 순서를 유지합니다.
    for i in range(len(array) - 1, -1, -1):
        digit = digit_at(array[i], divisor)
        counts[digit] -= 1
        result[counts[digit]] = array[i]
        if vis is not None:
            vis.step(array, f"LSD: divisor={divisor}, stable placement",
                     active=i, counts=counts, bucket=digit,
                     result=result, result_index=counts[digit])
    array[:] = result
    if vis is not None:
        vis.step(array, f"LSD: divisor={divisor}, digit pass complete")


def Radix_Sort_LSD(array, vis=None):
    if any(type(value) is not int or value < 0 for value in array):
        raise ValueError("LSD 기수 정렬은 0 이상의 정수만 지원합니다.")
    maximum = max(array, default=0)
    divisor = 1
    # 일의 자리에서 가장 높은 자리까지 순서대로 처리합니다.
    while maximum // divisor > 0:
        sort_digit(array, divisor, vis)
        divisor *= 10


def main():
    from sort_runner import run_sort
    run_sort(Radix_Sort_LSD, "Radix Sort LSD", "radix_lsd.json", "lsd")


if __name__ == "__main__":
    main()
