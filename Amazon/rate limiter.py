import time, collections

class RateLimiter:
    def __init__(self, max_number, interval):
        self.timeStamp = collections.defaultdict(collections.deque)
        self.interval = interval
        self.max_number = max_number

    def _clean(self, id, currTime):
        while self.timeStamp[id] and currTime - self.timeStamp[id][0] > self.interval:
            self.timeStamp[id].popleft()

    def call(self, id, times=1):
        if times > self.max_number:
            return False
        currTime = time.time()
        self._clean(id, currTime)
        if len(self.timeStamp[id]) + times <= self.max_number:
            self.timeStamp[id].extend([currTime] * times)
            return True
        else:
            return False

rateLimiter = RateLimiter(5, 2)
for i in range(10):
    print(rateLimiter.call(1,5))
time.sleep(1)
for i in range(10):
    print(rateLimiter.call(1))

# print('================')
# #
# class RateLimiter2:
#     def __init__(self, max_number, interval):
#         self.allowance = collections.defaultdict(lambda : max_number)
#         self.last_check = collections.defaultdict(lambda : -float('inf'))
#         self.interval = interval
#         self.max_number = max_number
#         self.rate = self.max_number / self.interval
#
#     def call(self, id):
#         currTime = time.time()
#         time_passed = currTime - self.last_check[id]
#         self.allowance[id] = min(self.max_number, self.allowance[id] + time_passed * self.rate)
#         if self.allowance[id] < 1:
#             return False
#         else:
#             self.allowance[id] -= 1
#             self.last_check[id] = currTime
#             return True
# rateLimiter = RateLimiter2(5, 2)
# for i in range(10):
#     print(rateLimiter.call(1))
# time.sleep(1)
# for i in range(10):
#     print(rateLimiter.call(1))


'''

Token Bucket: 
if you want just to drop messages when they arrive too quickly (instead of queuing them, which makes sense because the queue might get arbitrarily large):

rate = 5.0; // unit: messages
per  = 8.0; // unit: seconds
allowance = rate; // unit: messages
last_check = now(); // floating-point, e.g. usec accuracy. Unit: seconds

when (message_received):
  current = now();
  time_passed = current - last_check;
  last_check = current;
  allowance += time_passed * (rate / per);
  if (allowance > rate):
    allowance = rate; // throttle
  if (allowance < 1.0):
    discard_message();
  else:
    forward_message();
    allowance -= 1.0;
There are no datastructures, timers etc. in this solution and it works cleanly :) To see this, 'allowance' grows at speed 5/8 units per seconds at most, i.e. at most five units per eight seconds. Every message that is forwarded deducts one unit, so you can't send more than five messages per every eight seconds.

Note that rate should be an integer, i.e. without non-zero decimal part, or the algorithm won't work correctly (actual rate will not be rate/per). E.g. rate=0.5; per=1.0; does not work because allowance will never grow to 1.0. But rate=1.0; per=2.0; works fine.
'''