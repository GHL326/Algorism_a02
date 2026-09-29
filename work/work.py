import json
from pathlib import Path


DATA_FILE = Path(__file__).parent / "data" / "elementary_sort.json"

def Bubble_Sort(array):
    n = len(array)

    #버블 정렬 알고리즘
    for b in range(n):
        for i in range(0,n-b-1):
            if array [i] > array[i+1]:
                array[i], array[i+1] = array [i+1], array[i]


def main():

    # JSON 파일의 첫 번째 데이터 불러오기
    data = json.loads(DATA_FILE.read_text(encoding="utf-8-sig"))
    array = data["datasets"][0]["values"]

    #정렬 알고리즘 실행
    Bubble_Sort(array)

    #결과 출력
    print("Sorted array is:", array)


if __name__ == "__main__":
    main()
