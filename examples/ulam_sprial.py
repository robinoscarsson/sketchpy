from kanvas.core import run

DIRECTIONS = [(1,0), (0,-1), (-1,0), (0,1)]  # right, up, left, down

def is_prime(n):
    if n <= 1:
        return False
    if n % 2 == 0:
        return n == 2
    r = int(n**0.5)
    f = 3
    while f <= r:
        if n % f == 0:
            return False
        f += 2
    return True

def setup(model):
    model.clear(20)

    step_px = 4
    x = model.w // 2
    y = model.h // 2

    n = 1
    dir_idx = 0
    steps_in_leg = 1
    steps_taken = 0
    legs_done_at_length = 0

    while 0 <= x < model.w and 0 <= y < model.h:
        if is_prime(n):
            model.pixel(x, y, 255, 255, 255)

        dx, dy = DIRECTIONS[dir_idx]
        x += dx * step_px
        y += dy * step_px

        n += 1
        steps_taken += 1

        if steps_taken == steps_in_leg:
            # sväng
            dir_idx = (dir_idx + 1) % 4
            steps_taken = 0
            legs_done_at_length += 1
            if legs_done_at_length == 2:
                steps_in_leg += 1
                legs_done_at_length = 0

def draw(model, frame, dt):
    pass

run(setup, draw, size=(800, 800), title="Ulam Spiral Demo (fixed)")
