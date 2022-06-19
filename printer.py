from escpos.printer import Serial, Usb
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
    serial = Usb(0x8866, 0x0100, 0)
    serial.text("Hello world\n")
    serial.barcode('1324354657687', 'EAN13', 64, 2, '', '')
    serial.cut()
