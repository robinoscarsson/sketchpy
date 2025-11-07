from .core import *


def main():
    def setup(model):
        model.clear(20)  # mörk bakgrund

    def draw(model, frame, dt):
        x = (frame // 2) % model.w
        for y in range(model.h):
            model.pixel(x, y, 255, 255, 255)

    run(setup, draw, size=(320, 200), title="Pixel Smoke")

if __name__ == "__main__":
    main()