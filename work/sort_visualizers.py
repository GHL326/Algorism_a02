"""pyvisalgo의 시각화 기능과 정렬 단계 표시 화면."""
from types import SimpleNamespace

import pygame
import pyvisalgo as va


class Controls:
    def handle_event(self, event):
        if event.type == pygame.QUIT or (
            event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
        ):
            raise SystemExit
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self.paused = not self.paused
            return True
        return super().handle_event(event)

    def wait(self, millis):
        # 정렬 도중에도 창 닫기와 일시정지를 처리합니다.
        remaining = max(1, millis / self.speed)
        clock = pygame.time.Clock()
        while remaining > 0 or self.paused:
            elapsed = clock.tick(60)
            for event in pygame.event.get():
                self.handle_event(event)
            if not self.paused:
                remaining -= elapsed


class DistributionVisualizer(Controls, va.Visualizer):
    """계수와 기수 정렬의 입력, 빈도/위치, 작업 배열을 표시합니다."""
    PAGE_SIZE = 40

    def __init__(self, title, array):
        super().__init__(title)
        self.config.screen_width = 1200
        self.config.screen_height = 780
        self.config.font_size = 16
        self.apply_config()
        self.array = array
        self.message = "Ready"
        self.active = None
        self.result = None
        self.result_index = None
        self.counts = []
        self.labels = []
        self.bucket = None
        self.page = self.result_page = 0

    def step(self, array, message, active=None, counts=None, labels=None,
             result=None, result_index=None, bucket=None, delay=500):
        self.array = array
        self.message = message
        self.active = active
        self.result = result
        self.result_index = result_index
        self.counts = counts if counts is not None else []
        self.labels = labels if labels is not None else list(range(len(self.counts)))
        self.bucket = bucket
        if active is not None:
            self.page = active // self.PAGE_SIZE
        if result_index is not None:
            self.result_page = result_index // self.PAGE_SIZE
        self.draw()
        if delay:
            self.wait(delay)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key in (pygame.K_LEFT, pygame.K_RIGHT):
            delta = -1 if event.key == pygame.K_LEFT else 1
            last = max(0, (len(self.array) - 1) // self.PAGE_SIZE)
            self.page = min(last, max(0, self.page + delta))
            self.result_page = self.page
            self.draw()
            return True
        return super().handle_event(event)

    def draw_grid(self, values, y, page, active, label):
        if values is None:
            return
        start = page * self.PAGE_SIZE
        end = min(len(values), start + self.PAGE_SIZE)
        self.draw_text(f"{label} [{start}:{end}] / {len(values)}",
                       [36, y - 26], center=False)
        for index in range(start, end):
            offset = index - start
            x = 36 + (offset % 10) * 112
            row_y = y + (offset // 10) * 38
            color = (255, 216, 135) if index == active else (231, 240, 250)
            value = values[index]
            text = "-" if value is None else ('""' if value == "" else str(value))
            # 긴 문자열은 셀 안에서 줄이고 전체 값은 아래에 표시합니다.
            if len(text) > 11:
                text = text[:9] + ".."
            self.draw_box([x, row_y, 108, 34], text, body_color=color)
        if active is not None and 0 <= active < len(values):
            self.draw_text(f"index {active}: {values[active]!r}"[:120],
                           [36, y + 155], center=False)

    def draw_content(self):
        self.draw_text(self.message, [36, 22], center=False, font=self.big_font)
        self.draw_text("Orange: current item | Counts: frequency or placement boundary",
                       [36, 65], center=False)
        self.draw_grid(self.array, 120, self.page, self.active, "Array")
        if self.counts:
            start = (self.bucket // 32) * 32 if self.bucket is not None else 0
            self.draw_text(f"Buckets [{start}:{min(start + 32, len(self.counts))}]",
                           [36, 325], center=False)
            for index in range(start, min(start + 32, len(self.counts))):
                offset = index - start
                x = 36 + offset % 16 * 70
                y = 375 + offset // 16 * 55
                self.draw_text(str(self.labels[index]), [x + 32, y - 13])
                color = (255, 216, 135) if index == self.bucket else (225, 244, 228)
                self.draw_box([x, y, 64, 30], str(self.counts[index]), body_color=color)
        self.draw_grid(self.result, 520, self.result_page, self.result_index, "Work array")
        self.draw_text("1-9: speed | Space: pause | Left/Right: page | Esc: close",
                       [36, 738], center=False)


def create_visualizer(kind, title, array):
    if kind in ("count", "lsd", "msd"):
        return DistributionVisualizer(title, array)
    classes = {
        "selection": va.SelectionSortVisualizer,
        "insertion": va.InsertionSortVisualizer,
        "shell": va.ShellSortVisualizer,
        "heap": va.HeapSortVisualizer,
    }
    visualizer_type = type("ControlledVisualizer", (Controls, classes[kind]), {})
    vis = visualizer_type(title)
    vis.setup(SimpleNamespace(array=array))
    return vis
