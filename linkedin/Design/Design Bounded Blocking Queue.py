from threading import Semaphore, Lock, Condition
import collections
class BoundedBlockingQueue(object):
    # deque is thread-safe, so we don't need to use self.lock

    def __init__(self, capacity: int):
        self.en = Semaphore(capacity)
        self.de = Semaphore(0)
        self.lock = Lock()
        self.dq = collections.deque()

    def enqueue(self, element: int) -> None:
        self.en.acquire()
        self.lock.acquire()
        self.dq.appendleft(element)
        self.lock.release()
        self.de.release()

    def dequeue(self) -> int:
        self.de.acquire()
        self.lock.acquire()
        res = self.dq.pop()
        self.lock.release()
        self.en.release()
        return res

    def size(self) -> int:
        return len(self.dq)

    def peek(self):
        with self.lock:
            if len(self.dq) == 0:
                raise Exception('Empty Queue!')
            return self.dq[0]

from collections import deque
from threading import Lock


class BoundedBlockingQueue2(object):

    def __init__(self, capacity: int):
        self.en, self.de = Lock(), Lock()
        self.q = deque()
        self.capacity = capacity
        self.de.acquire()

    def enqueue(self, element: int) -> None:
        self.en.acquire()
        self.q.append(element)
        if len(self.q) < self.capacity:
            self.en.release()
        if self.de.locked():
            self.de.release()

    def dequeue(self) -> int:
        self.de.acquire()
        val = self.q.popleft()
        if len(self.q):
            self.de.release()
        if self.en.locked():
            self.en.release()
        return val

    def size(self) -> int:
        return len(self.q)

'''
// Imp with synchronzied block and volatile
class BoundedBlockingQueue {
    private final int[] queue;
    private volatile int size = 0;
    private int end = 0, start = 0;
    public BoundedBlockingQueue(int capacity) {
        this.queue = new int[capacity];
    }
    
    public void enqueue(int element) throws InterruptedException {
        synchronized (this) {
            while(size == queue.length) {
                wait();
            }
            queue[end++] = element;
            size++;
            end %= queue.length;
            notifyAll();
        }
    }
    
    public int dequeue() throws InterruptedException {
        synchronized (this) {
            while(size == 0) {
                wait();
            }
            int res = queue[start++];
            size--;
            start %= queue.length;
            notifyAll();
            return res;
        }
    }
    
    public int size() {
        return size;
    }
} 

// Imp with ReentrantLock and Condition variable
class BoundedBlockingQueue {
    private final int[] queue;
    private volatile int size = 0;
    private int end = 0, start = 0;
    private ReentrantLock lock = new ReentrantLock();
    private Condition full = lock.newCondition();
    private Condition empty = lock.newCondition();
    
    public BoundedBlockingQueue(int capacity) {
        this.queue = new int[capacity];
    }
    
    public void enqueue(int element) throws InterruptedException {
        lock.lock();
            
        try{
            while(size == queue.length) {
                full.await();
            }
            queue[end++] = element;
            size++;
            end %= queue.length;
            
            empty.signalAll();
        }finally{
            lock.unlock();
        }
    }
    
    public int dequeue() throws InterruptedException {
        lock.lock();
        try{
            while(size == 0) {
                empty.await();
            }从 
            int res = queue[start++];
            size--;
            start %= queue.length;
            full.signalAll();
            return res;
        }finally {
            lock.unlock();
        }
    }
    
    public int size() {
        return size;
    }
} 

// Imp with Semaphore
class BoundedBlockingQueue {
    private final int[] queue;
    private volatile int size = 0;
    private int end = 0, start = 0;
    Semaphore enqSem, deqSem, lockSem;
    
    public BoundedBlockingQueue(int capacity) {
        this.queue = new int[capacity];
        enqSem = new Semaphore(capacity);
        deqSem = new Semaphore(0);
        lockSem = new Semaphore(1);
    }
    
    public void enqueue(int element) throws InterruptedException {
        enqSem.acquire();
        lockSem.acquire();
        
        queue[end++] = element;
        size++;
        end %= queue.length;
        
        lockSem.release();
        deqSem.release();
    }
    
    public int dequeue() throws InterruptedException {
        deqSem.acquire();
        lockSem.acquire();
        
        int res = queue[start++];
        size--;
        start %= queue.length;
        
        lockSem.release();
        enqSem.release();
        return res;
    }
    
    public int size() {
        return size;
    }
}

'''