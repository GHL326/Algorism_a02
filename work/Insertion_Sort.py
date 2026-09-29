import json
from pathlib import Path


DATA_FILE = Path(__file__).parent / "data" / "elementary_sort.json"


def insert_at(array, end):
    """정렬된 앞부분에 array[end]를 끼워 넣습니다."""
    value = array[end]
    i = end - 1
    # 같은 값은 이동하지 않으므로 기존 순서가 유지됩니다.
    while i >= 0 and array[i] > value:
        array[i + 1] = array[i]
        i -= 1
    array[i + 1] = value


def Insertion_Sort(array):
    # 첫 원소 하나는 이미 정렬된 구간입니다.
    for end in range(1, len(array)):
        insert_at(array, end)


def main():
    data = json.loads(DATA_FILE.read_text(encoding="utf-8-sig"))
    dataset = data["datasets"][0]
    array = dataset["values"][:]
    print("Original array is:", array)
    Insertion_Sort(array)
    print("Sorted array is:", array)


if __name__ == "__main__":
    main()
