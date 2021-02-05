'''
package linkedin;

import java.io.Closeable;
import java.io.IOException;
import java.util.LinkedList;
import java.util.List;
import java.util.concurrent.*;

abstract class Input {
    abstract Output output();
}

abstract class Output {
    abstract Output add(Output o);
}

public class MergeCompute<O extends Output, I extends Input> implements Closeable {
    private ExecutorService executor;

    public MergeCompute(int k) {
        executor = Executors.newFixedThreadPool(k);
    }

    public Output mergeAll(List<Input> inputs) {
        List<Future<Output>> futures = new LinkedList<>();
        for (Input input : inputs) {
            final Input source = input;
            futures.add(executor.submit(() -> Util.compute(source)));
        }
        try {
            while (futures.size() > 1) {
                futures.add(executor.submit(() -> Util.merge(futures.remove(0).get(), futures.remove(0).get())));
            }
            return futures.get(0).get();
        } catch (InterruptedException | ExecutionException e) {
            e.printStackTrace();
        }
        return null;
    }

    @Override
    public void close() throws IOException {
        this.executor.shutdown();
    }
}

class Util {
    static Output compute(Input in) {
        return in.output();
    }

    static Output merge(Output o1, Output o2) {
        return o1.add(o2);
    }
}
'''
from concurrent import futures
from collections import deque


class Output:
    def __init__(self, x):
        self.x = x
    def __repr__(self):
        return str(self.x)

class Input:
    def __init__(self, x):
        self.x = x
    def __repr__(self):
        return str(self.x)

def compute(input):
    return Output(input.x)


def merge(output1, output2):
    return Output(output1.x + output2.x)


class MergeCompute:
    def __init__(self, k):
        self.executor = futures.ThreadPoolExecutor(max_workers=k)

    def mergeAll(self, inputs):
        futures = deque([self.executor.submit(compute, i) for i in inputs])
        while len(futures) > 1:
            futures.append(self.executor.submit(merge, futures.popleft().result(), futures.popleft().result()))
        return futures[0].result()


mc = MergeCompute(5)
inputs = [Input(i) for i in range(100)]
print(mc.mergeAll(inputs))

'''
Advantages of a Thread Pool
Some of the advantages of using thread pool when programming in Java are:

Better performance
Saves time
No need to create a thread again and again
Easy to access
Real-time usage
Now, let us check out the disadvantages of the thread pool.

Disadvantages of the Thread Pool
Some of the disadvantages of using thread pool when programming are:

There is no control over the priority and state of the thread you are working with.
There is no stable identity given to the thread, no track can be kept.
When there is a high demand for the thread pool, the process may be deleted.
The thread pool can not work well when two threads are working in parallel.
There are several situations where the application code can be affected by another application code, despite robust application isolation.
'''