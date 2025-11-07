import time

def run(setup, draw, target_fps=60):
    setup()
    frameCount = 0
    last = time.perf_counter()
    running = True
    while running:
        now = time.perf_counter()
        delta_ms = (now - last) * 1000.0
        last = now
        draw(frameCount, delta_ms)
        frameCount += 1
        if frameCount % 100 == 0:
            print(f"Frame: {frameCount}, Delta ms: {delta_ms:.2f}") 
        time.sleep(max(0, (1/target_fps) - (time.perf_counter() - now)))