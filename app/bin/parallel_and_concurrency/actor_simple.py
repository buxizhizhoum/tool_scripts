#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
refer actor model from python cookbook 3rd edition
"""
import datetime
import threading
import time
from Queue import Queue
from Queue import Empty

QSIZE = 10


class ActorExit(Exception):
    pass


class Actor(object):
    """
    class of Actor

    two ways to stop a thread.
        1. set self._running to False
        2. send ActorExit

        the first version of _run, close the threads with method 1,
        the second version of _run close the threads with method 2.
    """
    def __init__(self, qsize=None):
        self._mailbox = Queue(qsize)
        self._running = True

    def send(self, msg):
        self._mailbox.put(msg)

    def recv(self):
        """
        receive msg, if msg is ActorExit, raise ActorExit exception.

        if there is no timeout parameter, close() method could not close
        thread since thread will block at self._mailbox.get()
        :return:
        """
        # if there is no timeout parameter, close() method could not close
        # thread since thread will block at self._mailbox.get()
        msg = self._mailbox.get(timeout=1)  # attention: there is timeout

        if msg is ActorExit:
            raise ActorExit()
        return msg

    def close(self):
        self._running = False
        print("close thread")

    def start(self):
        t = threading.Thread(target=self._run)

        # t.daemon = True  # think more here
        t.start()

    def run(self):
        while True:
            msg = self.recv()
            print(msg)

    def _run(self):
        """
        close all threads by set flag which all threads are polling
        :return:
        """
        while self._running:
            try:
                self.run()
            except ActorExit:
                print("exit")
                self._running = False  # this will kill all thread
            except Empty:
                print("queue is empty")
                continue

# another method to close thread when there is ActorExit signal
    # def _run(self):
    #     """
    #     close a thread if ActorExit exception is captured.
    #
    #     if the ActorExit is put back to queue, all of the threads that listen
    #     to the queue will be closed.
    #     :return:
    #     """
    #     while self._running:
    #         try:
    #             self.run()
    #         except ActorExit:
    #             print("exit")
    #             # put the ActorExit msg back into queue, and all of the threads
    #             # that listen to the queue will be closed
    #             self._mailbox.put(ActorExit)
    #             break


class PrintActor(Actor):
    """
    the actor that do some real things.
    """
    def run(self):
        while True:
            msg = self.recv()
            print(msg)
            # write file, could be any thing.
            self.write_file(msg)
            time.sleep(0.1)

    @staticmethod
    def write_file(msg):
        with open("tmp.txt", "a") as f:
            now_dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write("{}, {}".format(now_dt, msg))
            f.write("\n")
            f.flush()


if __name__ == "__main__":
    p = PrintActor(QSIZE)
    p.start()
    # start a thread for each send() with no block.
    p.send(1)
    p.send(2)
    # program will reach here with no block at send() before.
    print("send complete")
    time.sleep(2)

    # send ActorExit and close() are two method to close a thread

    # p.send(ActorExit)  # send ActorExit to end the thread.

    # this could also stop the thread, but if the get() method of queue
    # is blocking forever, the thread will have no chance to
    # check running flag which will leave an never close thread.
    p.close()
