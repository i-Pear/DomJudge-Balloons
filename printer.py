from escpos.printer import Serial, Usb
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
    serial = Usb(0x8866, 0x0100, 0)
    serial.text("Hello world\n")
    serial.barcode('1324354657687', 'EAN13', 64, 2, '', '')
    serial.cut()
