import json
from pathlib import Path


DATA_FILE = Path(__file__).parent / "data" / "elementary_sort.json"


def insert_with_gap(array, end, gap):
    """gap만큼 떨어진 원소들 사이에 현재 값을 삽입합니다."""
    value = array[end]
    i = end - gap
    while i >= 0 and array[i] > value:
        array[i + gap] = array[i]
        i -= gap
    array[i + gap] = value


def Shell_Sort(array):
    gap = len(array) // 2
    # 간격을 반씩 줄이고 마지막에는 gap=1로 전체를 정렬합니다.
    while gap > 0:
        for end in range(gap, len(array)):
            insert_with_gap(array, end, gap)
        gap //= 2


def main():
    data = json.loads(DATA_FILE.read_text(encoding="utf-8-sig"))
    dataset = data["datasets"][0]
    array = dataset["values"][:]
    print("Original array is:", array)
    Shell_Sort(array)
    print("Sorted array is:", array)


if __name__ == "__main__":
    main()
