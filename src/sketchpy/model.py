import numpy as np

class Model:
    def __init__(self, w: int, h: int):
        self.w, self.h = w, h
        self.fb = np.zeros((w, h, 3), dtype=np.uint8)  # (W,H,RGB)

    def clear(self, r: int, g: int = None, b: int = None):
        if g is None: g = b = r
        self.fb[:] = (r, g, b)

    def pixel(self, x: int, y: int, r: int, g: int, b: int):
        if 0 <= x < self.w and 0 <= y < self.h:
            self.fb[x, y] = (r, g, b)