'''
There are two kinds of threads, oxygen and hydrogen. Your goal is to group these threads to form water molecules. There is a barrier where each thread has to wait until a complete molecule can be formed. Hydrogen and oxygen threads will be given releaseHydrogen and releaseOxygen methods respectively, which will allow them to pass the barrier. These threads should pass the barrier in groups of three, and they must be able to immediately bond with each other to form a water molecule. You must guarantee that all the threads from one molecule bond before any other threads from the next molecule do.

In other words:

If an oxygen thread arrives at the barrier when no hydrogen threads are present, it has to wait for two hydrogen threads.
If a hydrogen thread arrives at the barrier when no other threads are present, it has to wait for an oxygen thread and another hydrogen thread.
We don’t have to worry about matching the threads up explicitly; that is, the threads do not necessarily know which other threads they are paired up with. The key is just that threads pass the barrier in complete sets; thus, if we examine the sequence of threads that bond and divide them into groups of three, each group should contain one oxygen and two hydrogen threads.

Write synchronization code for oxygen and hydrogen molecules that enforces these constraints.
'''

from threading import Barrier, Semaphore
class H2O:
    '''
    Barrier objects in python are used to wait for a fixed number of thread to complete execution before any particular thread can proceed forward with the execution of the program. Each thread calls wait() function upon reaching the barrier. The barrier is responsible for keeping track of the number of wait() calls. If this number goes beyond the number of threads for which the barrier was initialized with, then the barrier gives a way to the waiting threads to proceed on with the execution. All the threads at this point of execution, are simultaneously released.

Barriers can even be used to synchronize access between threads. However, generally a barrier is used to combine the output of threads. A barrier object can be reused multiple times for the exact same number of threads that it was initially initialized for.p
    '''
    def __init__(self):
        self.b = Barrier(3)
        self.h = Semaphore(2)
        self.o = Semaphore(1)

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        self.h.acquire()
        self.b.wait()
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        releaseHydrogen()
        self.h.release()

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        self.o.acquire()
        self.b.wait()
        # releaseOxygen() outputs "O". Do not change or remove this line.
        releaseOxygen()
        self.o.release()

# if we need to ensure 2 H appear before 1 O
from threading import Lock


class H2O:
    def __init__(self):
        self.h_cnt = 0
        self.o_cnt = 0
        self.h_lock = Lock()
        self.o_lock = Lock()
        self.o_lock.acquire()

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:

        # releaseHydrogen() outputs "H". Do not change or remove this line.
        self.h_lock.acquire()
        self.h_cnt += 1
        releaseHydrogen()
        if self.h_cnt - 2 * self.o_cnt == 2:
            self.o_lock.release()
        else:
            self.h_lock.release()

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:

        # releaseOxygen() outputs "O". Do not change or remove this line.
        self.o_lock.acquire()
        self.o_cnt += 1
        releaseOxygen()
        self.h_lock.release()

'''
import java.util.concurrent.*;
class H2O {
    
    Semaphore h, o;
    public H2O() {
        h = new Semaphore(2, true);
        o = new Semaphore(0, true);
    }

    public void hydrogen(Runnable releaseHydrogen) throws InterruptedException {
		h.acquire();
        releaseHydrogen.run();
        o.release();
        
    }

    public void oxygen(Runnable releaseOxygen) throws InterruptedException {
        o.acquire(2);
		releaseOxygen.run();
        h.release(2);
    }
}

class H2O {
   
    private Object lock = new Object();
    private int counter =0;
    public H2O() {
        
    }

    public void hydrogen(Runnable releaseHydrogen) throws InterruptedException {
		
     synchronized (lock) {
            while(counter==2){
                lock.wait();
            }
            releaseHydrogen.run();
            counter++;
            lock.notifyAll();
      }
    }

    public void oxygen(Runnable releaseOxygen) throws InterruptedException {
        synchronized (lock) {
            while(counter!=2){
                lock.wait();
            }
            releaseOxygen.run();
            counter=0;
            lock.notifyAll();
      }
        
    }
}
'''