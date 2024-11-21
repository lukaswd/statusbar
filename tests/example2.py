import time

from pystatusbar import StatusBar

if __name__ == '__main__':
    format_start = "\033[7m This is a test {WORD}bar with lines: {i}\033[27m"

    bar = StatusBar(format_start=format_start, fill="\033[7m \033[27m", i=0, WORD="")
    bar.start()
    for i in range(50):
        print(f"Test Line {i}")
        if i % 10 == 0:
            bar.update(i=i)

        if i == 25:
            bar.update(WORD="status")

        time.sleep(0.1)
    bar.stop()