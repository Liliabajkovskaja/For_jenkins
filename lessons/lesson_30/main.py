import subprocess
import time

# # system command
# result = subprocess.run('dir', shell=True, capture_output=False, text=False, check=False)
# print(result.stdout)

# # run script
# result = subprocess.run(['python', r'F:\jenkins_lessons\Tests_0324\lessons\lesson_31\some_files.py'],
#                         shell=True, capture_output=True, text=True, check=True)
# print(result.stdout)
# print(result.stderr)

#
#
# #
# p = subprocess.Popen('python --help', stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
# p_out, p_errors = p.communicate()
# print(p_out)

# commands = [r'F:\jenkins_lessons\Tests_0324\.venv\Scripts\python', r'F:\jenkins_lessons\Tests_0324\lessons\lesson_31\redis_output.py']
#
# p = subprocess.Popen(commands, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
#
# time.sleep(10)
#
#
# for output in p.stdout:
#     print(f'redis line:  {output}')
#     if 'Record was created' in output:
#         p.terminate()


# threading
# Thread: target, args, start, join

import threading
import math


def get_factorial(nums: [int]):

    # fats = []
    # for num in nums:
    #     fats.append(math.factorial(num))
    # return fats

    time.sleep(1)

    print([math.factorial(num) for num in nums])

import time

# time_start = time.time()
#
# for k in range(10):
#     time.sleep(1)
#     get_factorial([100, 200, 300, 500, 1231])
#
# print(f'result time is {time.time() - time_start}')


import threading

# threads = []
#
#
# for k in range(10):
#     threads.append(threading.Thread(target=get_factorial, args=[[100, 200, 300, 500, 1231]]))
#
# time_start = time.time()
# for t in threads:
#     t.start()  # starts of thread
#
# for t in threads:
#     t.join()  # wait for finish
#
# print(f'result time is {time.time() - time_start}')


import threading

outputs = []


def append_number(num):

    time.sleep(3)
    for k in range(10):
        print('-'*20)
        print(num)
        outputs.append(num)
        print(outputs)
        print('-' * 20)

import multiprocessing

if __name__ == '__main__':

    print(multiprocessing.cpu_count())

    # process = [multiprocessing.Process(target=append_number, args=[k]) for k in range(4)]
    #
    # [p.start() for p in process]

#
# t = threading.Thread(target=append_number, args=[1])
#
# ts = time.time()
# t.start()
# t.join(timeout=2)
#
# if t.is_alive():
#     print('is alive')
# print(time.time() - ts)


# thrs = [threading.Thread(target=append_number, args=[k]) for k in range(4)]
# #
# [t.start() for t in thrs]
#
# [t.join(timeout=1) for t in thrs]

# threading
# example: time, output math.factorial_number
# lock.acquire

#
# from threading import Thread, Lock
#
# with open('thread_test', 'w') as f:
#     f.write('start\n')
#
# lock = Lock()
#
# def read_write(num):
#     time.sleep(1)
#     lock.acquire()
#     text = f'Thread {num} '
#     with open('thread_test', 'a') as f:
#         f.write(text)
#
#     with open('thread_test', 'r') as f:
#         x = f.read()
#
#     lock.release()
#     print(f"""
#     --------------------
#     write - {text}
#     read = {x}
#     -------------------""")
#
# trs = [Thread(target=read_write, args=[k]) for k in range(20)]
#
# [t.start() for t in trs]


# multiprocessing.Process
# Pool(processes=multiprocessing.cpu_count()
# import threading
#
# lock = threading.Lock()
#
# with open('thread_test', 'w') as f:
#     pass
#
#
# def read_write(num):
#     # lock.acquire()
#     text = f'Thread {num} '
#     with open('thread_test', 'a') as f:
#         f.write(text)
#
#     with open('thread_test', 'r') as f:
#         x = f.read()
#
#     # lock.release()
#     print(f"""
#     --------------------
#     write - {text}
#     read = {x}
#     -------------------""")
#
#
# thr = []
# for k in range(10):
#     thr.append(threading.Thread(target=read_write, args=[k]))
#
# for k in thr:
#     k.start()
