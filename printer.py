from escpos.printer import Serial
import queue


class print_pkg:
    pass


print_queue = queue.Queue()


def print_service():
    while True:
        cnt = print_queue.get()
        # print item


if __name__ == '__main__':
    # unit test
    serial = Serial('COM3', 38400, timeout=1)
    serial.text("Hello world\n")
    serial.barcode('1324354657687', 'EAN13', 64, 2, '', '')
    serial.cut()
