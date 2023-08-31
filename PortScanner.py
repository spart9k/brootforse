import socket
import threading
lock = threading.Lock()
#host = "IP address"
found = False
def check_port(port: int):
    global found
    socket_client = socket.socket()
    result = socket_client.connect_ex((host, port))
    if result == 0:
        print(f"найден открытый порт! {port}")
    socket_client.close()
def thread_task():
    global ports_to_check
    while ports_to_check and not found:
        lock.acquire()
        try:
            to_check = ports_to_check.pop(0)
        finally:
            lock.release()
        check_port(to_check)
ports_to_check = [port_num for port_num in range(22, 6001)]
threads = []
threads_count = int(input("Кол-во потоков: "))
for _ in range(threads_count):
    thread = threading.Thread(target=thread_task)
    threads.append(thread)
    thread.start()
for thread in threads:
    thread.join()
