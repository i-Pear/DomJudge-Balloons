import queue
import tempfile
import win32api
import win32print
import threading


class print_pkg:
    pass


print_queue = queue.Queue()


def print_str(s):
    filename = tempfile.mktemp(".txt")
    open(filename, "w", encoding='utf-8').write(s)
    win32api.ShellExecute(
        0,
        "print",
        filename,
        '/d:"%s"' % win32print.GetDefaultPrinter(),
        ".",
        0
    )


class PrintService(threading.Thread):
    def run(self) -> None:
        while True:
            cnt = print_queue.get()
            print_str(cnt)


if __name__ == '__main__':
    # unit test
    print_str("This is a test...")
    print_str("""
    ------- Balloon Request -------
时间：14：20
题号：A
颜色：绿色
座位号：A区204
⬜⬜⬜⬜⬜⬜⬜⬜ ⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜ ⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜ ⬜⬜⬜⬜⬜⬛⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜ ⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜ ⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜ ⬜⬜⬜⬜⬜⬜⬜⬜⬜
    ----- Balloon Request End -----
    """)
