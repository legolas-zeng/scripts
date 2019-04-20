# coding=utf-8
# @Time    : 2019/4/18 17:22
# @Author  : zwa
import threading
import time
from multiprocessing import Pool
from queue import Queue

import bs4
import requests

PRIME_NUM = 1000000
PRIME_CNT = 10

REQUEST_URL = 'https://www.baidu.com/'
REQUEST_CNT = 100


def do_request(current_url):
    print('.', end='', flush=True)
    res = requests.get(current_url)
    res.raise_for_status()


def sum_prime(num):
    print('.', end='', flush=True)
    sum_of_primes = 0
    ix = 2
    while ix <= num:
        if is_prime(ix):
            sum_of_primes += ix
        ix += 1

    return sum_of_primes


def process_cpu_queue(queue):
    while True:
        num = queue.get()
        sum_prime(num)
        queue.task_done()


def process_io_queue(queue):
    while True:
        current_url = queue.get()
        do_request(current_url)
        queue.task_done()


def is_prime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i*i <= num:
        if num % i == 0 or num % (i+2) == 0:
            return False
        i += 6
    return True


def multi_threading_io(thread_cnt):
    queue = Queue()
    url_list = [REQUEST_URL] * REQUEST_CNT

    for i in range(thread_cnt):
        t = threading.Thread(target=process_io_queue, args=(queue,))
        t.daemon = True
        t.start()

    start = time.time()

    for current_url in url_list:
        queue.put(current_url)

    queue.join()

    print('\n{0} threading, execute time = {1:.5f} s'.format(
        thread_cnt, time.time() - start))


def multi_processing_io(process_cnt):
    url_list = [REQUEST_URL] * REQUEST_CNT
    start = time.time()

    with Pool(process_cnt) as p:
        p.map(do_request, url_list)
    print('\n{0} processing, execute time = {1:.5f} s'.format(
        process_cnt, time.time() - start))


def multi_threading_cpu(thread_cnt):
    start = time.time()
    queue = Queue()
    for i in [PRIME_NUM]*PRIME_CNT:
        queue.put(i)

    for i in range(thread_cnt):
        t = threading.Thread(target=process_cpu_queue, args=(queue,))
        t.daemon = True
        t.start()

    queue.join()

    print('\n{0} threading, execute time = {1:.5f} s'.format(
        thread_cnt, time.time() - start))


def multi_processing_cpu(process_cnt):
    start = time.time()
    with Pool(process_cnt) as p:
        p.map(sum_prime, [PRIME_NUM]*PRIME_CNT)
    print('\n{0} processing, execute time = {1:.5f} s'.format(
        process_cnt, time.time() - start))


if __name__ == '__main__':
    print('>>> multi_threading_io, total {} requests'.format(REQUEST_CNT))
    multi_threading_io(1)
    multi_threading_io(2)
    multi_threading_io(5)

    print('\n>>> multi_processing_io, total {} requests'.format(REQUEST_CNT))
    multi_processing_io(1)
    multi_processing_io(2)
    multi_processing_io(5)

    print('\n>>> multi_threading_cpu, total {} tasks'.format(PRIME_CNT))
    multi_threading_cpu(1)
    multi_threading_cpu(2)
    multi_threading_cpu(5)

    print('\n>>> multi_processing_cpu, total {} tasks'.format(PRIME_CNT))
    multi_processing_cpu(1)
    multi_processing_cpu(2)
    multi_processing_cpu(5)