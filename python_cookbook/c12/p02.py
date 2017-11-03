from threading import Thread, Event
import time
import threading

"""
判断线程是否已经启动
"""

# Code to execute in an independent thread
def countdown(n, started_evt):
    print('countdown starting')
    started_evt.set()
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(1)


# 通过event协调线程, 使主线程(prac1)等到countdown函数输出启动信息后, 才继续执行
def prac1():
    # Create the event object that will be used to signal startup
    started_evt = Event()

    # Launch the thread and pass the startup event
    print('Launching countdown')
    t = Thread(target=countdown, args=(10,started_evt))
    t.start()

    # Wait for the thread to start
    started_evt.wait()
    print('countdown is running')


# ---------------------------------------------------------------------------------------------

class PeriodicTimer:
    def __init__(self, interval):
        self._interval = interval
        self._flag = 0
        self._cv = threading.Condition()

    def start(self):
        t = threading.Thread(target=self.run)
        t.daemon = True
        t.start()

    def run(self):
        """
        Run the timer and notify waiting threads after each interval
        """
        while True:
            time.sleep(self._interval)
            with self._cv:
                self._flag ^= 1
                self._cv.notify_all()

    def wait_for_tick(self):
        """
        Wait for the next tick of the timer
        :return:
        """
        with self._cv:
            last_flag = self._flag
            while last_flag == self._flag:
                self._cv.wait()



# Two threads that synchronize on the timer
def countdown1(nticks, ptimer):
    while nticks > 0:
        ptimer.wait_for_tick()
        print('T-minus', nticks)
        nticks -= 1


def countup(last, ptimer):
    n = 0
    while n < last:
        ptimer.wait_for_tick()
        print('Counting', n)
        n += 1



if __name__ == '__main__':
    # prac1()

    # Example user of the timer
    ptimer = PeriodicTimer(1)
    ptimer.start()

    threading.Thread(target=countdown1, args=(10, ptimer)).start()
    threading.Thread(target=countup, args=(5, ptimer)).start()
