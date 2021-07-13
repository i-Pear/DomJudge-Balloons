import queue
import threading
import time
import printer

if __name__ == '__main__':
    print_service = printer.PrintService()
    print_service.start()

    for i in range(5):
        printer.print_queue.put(str(i))
        time.sleep(10)
