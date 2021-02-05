from threading import Condition, Lock, currentThread, Thread
from heapq import heappush, heappop
import time


# http://hg.openjdk.java.net/jdk8/jdk8/jdk/file/tip/src/share/classes/java/util/concurrent/DelayQueue.java
class DelayQueue:
    def __init__(self):
        self.heap = []
        self.lock = Lock()
        self.available = Condition(self.lock)
        '''
    //The leader is not used for minimizing awaitNanos, it is used for avoiding unnecessary wake up & sleep.
    // If you let all threads available.awaitNanos(delay) in take method, they will be called up simultaneously
    // but only one can really get element from the queue, the others will fall into sleeping again, which is unnecessary and resource-wasting.
    //
    //With Leader-Follower pattern, the leader available.awaitNanos(delay), the non-leader threads available.await().
    // So the leader will wake up first and retrieving an expried element, then signal another waiting thread if necessary. This is more efficient.
        '''
        self.leader_thread = None

    def put(self, task_id, delay):
        with self.lock:
            task = (time.time() + delay, task_id)
            heappush(self.heap, task)
            if task == self.heap[0]:
                # we need to execute the new inserted task next time, so we set the leader to None
                # and wake up all the threads to compete to become the leader
                self.leader_thread = None
                self.available.notifyAll()

    def take(self):
        with self.lock:
            try:
                while True:
                    if not self.heap or not self.heap[0]:
                        self.available.wait()
                    else:
                        delay = self.heap[0][0] - time.time()
                        if delay <= 0:
                            return heappop(self.heap)[1]
                        if self.leader_thread:  # there has already been a leader taking, so current consumer should wait
                            self.available.wait()
                        else:  # no leader, current thread can become a leader, it will wait for delay time and next time when it come back, will return
                            this_thread = currentThread()
                            self.leader_thread = this_thread
                            try:
                                self.available.wait(delay)
                            finally:
                                if self.leader_thread == this_thread:
                                    self.leader_thread = None
            finally:
                if not self.leader_thread and self.heap and self.heap[0]:
                    self.available.notifyAll()


'''
3. take()方法中为什么释放first
first = null; // don't retain ref while waiting
我们可以看到 Doug Lea 后面写的注释，那么这行代码有什么用呢？
如果删除这行代码，会发生什么呢？假设现在有3个消费者线程，
•	线程A进来获取first,然后进入 else 的 else ,设置了leader为当前线程A，并让A等待一段时间
•	线程B进来获取first, 进入else的阻塞操作,然后无限期等待，这时线程B是持有first引用的
•	线程A等待指定时间后被唤醒，获取对象成功，出队，这个对象理应被GC回收，但是它还被线程B持有着，GC链可达，所以不能回收这个first
•	只要线程B无限期的睡眠，那么这个本该被回收的对象就不能被GC销毁掉，那么就会造成内存泄露
'''
import random

target = []


def produce(delay_queue):
    for id in range(50):
        delay = random.randint(1, 100)
        delay_queue.put(id, delay)
        print('Put: ' + str(id), 'Delay: ' + str(delay), 'StartTime: ' + str(time.time() + delay))
        target.append((time.time() + delay, id))
        time.sleep(1)


res = []


def consume(delay_queue):
    while True:
        id = delay_queue.take()
        res.append(id)
        print('Take: ' + str(id))


delay_queue = DelayQueue()
Thread(target=produce, args=(delay_queue,)).start()
Thread(target=consume, args=(delay_queue,)).start()
target = [i for _, i in sorted(target)][:len(res)]
assert res == target
