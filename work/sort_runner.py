"""정렬 예제의 데이터 선택, 터미널 출력, 시각화 실행을 공통 처리합니다."""
import argparse
import json
from pathlib import Path


def run_sort(sort, title, filename, kind):
    parser = argparse.ArgumentParser(description=title)
    parser.add_argument("--no-vis", action="store_true", help="터미널 결과만 출력")
    parser.add_argument("--dataset", type=int, default=1, help="JSON 데이터 번호 (1부터)")
    parser.add_argument("--data", type=Path, help="다른 JSON 데이터 파일")
    parser.add_argument("--speed", type=int, choices=range(1, 201), default=5,
                        help="시각화 속도 (기본 5)")
    args = parser.parse_args()
    path = args.data or Path(__file__).parent / "data" / filename
    datasets = json.loads(path.read_text(encoding="utf-8-sig"))["datasets"]
    if not 1 <= args.dataset <= len(datasets):
        parser.error(f"--dataset은 1~{len(datasets)} 범위여야 합니다.")
    dataset = datasets[args.dataset - 1]
    values = dataset["values"] if "values" in dataset else dataset["data"]["array"]
    array = list(values)
    print("Dataset:", dataset["name"])
    print("Original array is:", array, flush=True)

    if args.no_vis or not array:
        sort(array)
        print("Sorted array is:", array)
        return

    import pygame
    from sort_visualizers import create_visualizer

    print("숫자 1~9: 속도 / Space: 일시정지 / Esc: 종료", flush=True)
    try:
        vis = create_visualizer(kind, title, array)
        vis.speed = args.speed
        vis.draw()
        sort(array, vis)
        if hasattr(vis, "step"):
            vis.step(array, "Complete - Left/Right: browse array", delay=0)
        print("Sorted array is:", array, flush=True)
        pygame.display.set_caption(title + " - Complete (Esc to close)")
        clock = pygame.time.Clock()
        while True:
            for event in pygame.event.get():
                vis.handle_event(event)
            clock.tick(30)
    finally:
        pygame.quit()
