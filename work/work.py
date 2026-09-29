import json
from pathlib import Path
from types import SimpleNamespace

import pygame
import pyvisalgo as va


DATA_FILE = Path(__file__).parent / "data" / "elementary_sort.json"


class BubbleVisualizer(va.BubbleSortVisualizer):
    def handle_event(self, event):
        # 정렬 도중 창을 닫아도 즉시 종료합니다.
        if event.type == pygame.QUIT or (
            event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
        ):
            raise SystemExit
        return super().handle_event(event)


def Bubble_Sort(array, vis=None):
    n = len(array)

    #버블 정렬 알고리즘
    for b in range(n):
        for i in range(0,n-b-1):
            if vis is not None:
                vis.compare(i, i + 1)
            if array [i] > array[i+1]:
                if vis is not None:
                    vis.swap(i, i + 1)
                array[i], array[i+1] = array [i+1], array[i]
                if vis is not None:
                    vis.draw()
        if vis is not None:
            vis.bubble_end(n - b - 1)


def main():

    # JSON 파일의 첫 번째 데이터 불러오기
    data = json.loads(DATA_FILE.read_text(encoding="utf-8-sig"))
    array = data["datasets"][0]["values"]

    print("Original array is:", array)
    print("시각화: 숫자 1~9로 속도 변경, Esc 또는 창 닫기로 종료", flush=True)

    try:
        vis = BubbleVisualizer("Bubble Sort")
        vis.speed = 5
        vis.setup(SimpleNamespace(array=array))
        vis.draw()

        # 비교 및 교환 과정을 시각화하면서 정렬합니다.
        Bubble_Sort(array, vis)

        print("Sorted array is:", array, flush=True)
        pygame.display.set_caption("Bubble Sort - Complete (Esc to close)")

        # 정렬된 결과를 창에 유지합니다.
        while True:
            vis.handle_event(pygame.event.wait())
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
