'''
All O`one Data Structure
'''
def sliding_window_mean(A, k):
    s = 0
    res = []
    for i, a in enumerate(A):
        s += a
        if i >= k - 1:
            res.append(s / k)
            s -= A[i - k + 1]
    return res

def helper(A, k):
    res = []
    for i in range(len(A) - k + 1):
        res.append(sum(A[i : i + k]) / k)
    return res

class Node:

    def __init__(self, val):
        self.val = val
        self.pre = None
        self.nxt = None
        self.keySet = set()


class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = Node(-float('inf'))
        self.tail = Node(float('inf'))
        self.keyCount = {}
        self.countNode = {}
        self.tail.pre = self.head
        self.head.nxt = self.tail

    def _change(self, key, num):
        curCount = self.keyCount[key]
        curNode = self.countNode[curCount]
        self.keyCount[key] += num
        if curCount + num not in self.countNode:
            newNode = Node(curCount + num)
            self.countNode[curCount + num] = newNode
            self._addAfter(curNode if num == 1 else curNode.pre, newNode)
        else:
            newNode = self.countNode[curCount + num]
        newNode.keySet.add(key)
        self._removeKey(curNode, key)

    def _removeKey(self, node, key):
        node.keySet.remove(key)
        if not node.keySet:
            self._removeNode(node)

    def _removeNode(self, node):
        self.countNode.pop(node.val)
        node.pre.nxt, node.nxt.pre = node.nxt, node.pre

    def _addAfter(self, node, toAdd):
        nxt = node.nxt
        toAdd.nxt = nxt
        nxt.pre = toAdd
        toAdd.pre = node
        node.nxt = toAdd

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        if key not in self.keyCount:
            self.keyCount[key] = 1
            if 1 not in self.countNode:
                self._addAfter(self.head, Node(1))
            self.countNode[1] = self.head.nxt
            self.head.nxt.keySet.add(key)
        else:
            self._change(key, 1)

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        if key not in self.keyCount: return
        if self.keyCount[key] == 1:
            self._removeKey(self.countNode[1], key)
            self.keyCount.pop(key)
        else:
            self._change(key, -1)

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        return next(iter(self.tail.pre.keySet)) if self.head.nxt != self.tail else ''

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        return next(iter(self.head.nxt.keySet)) if self.head.nxt != self.tail else ''

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()

def sliding_window_mode(A, k):
    res = []
    cnt = 0
    ao = AllOne()
    for i, a in enumerate(A):
        ao.inc(a)
        cnt += 1
        if cnt == k:
            res.append(ao.getMaxKey())
            ao.dec(A[i - k + 1])
            cnt -= 1
    return res

print(sliding_window_mode([1,1,1,1,1,2,2,2,2,3,3,4,1,3,4], 3))
import collections
def helper(A, k):
    cnt = collections.Counter()
    res = []
    for i in range(len(A)):
        cnt[A[i]] += 1
        if i >= k - 1:
            mx = max(cnt.values())
            print(cnt)
            res.append([k for k in cnt if cnt[k] == mx][0])
        if i >= k - 1: cnt[A[i - k + 1]] -= 1
    return res

# Sliding Window Median
'''
class Solution {
    public double[] medianSlidingWindow(int[] nums, int k) {
        TreeSet<Integer> left = new TreeSet<>((a, b) -> nums[b] == nums[a] ? a - b : Integer.compare(nums[b], nums[a]));
        TreeSet<Integer> right = new TreeSet<>((a, b) -> nums[b] == nums[a] ? a - b : Integer.compare(nums[a], nums[b]));
        double[] res = new double[nums.length - k + 1];

        for (int i = 0; i < k; i++) {
            left.add(i);
        }
        balance(left, right);
        res[0] = getMedian(k, nums, left, right);

        int r = 1;
        for (int i = k; i < nums.length; i++) {
            if(!left.remove(i - k)) {
                right.remove(i - k);
            }
            right.add(i); 
            left.add(right.pollFirst());
            balance(left, right); 
            res[r] = getMedian(k, nums, left, right);
            r++;
        }

        return res;
    }
    
    private void balance(TreeSet<Integer> left, TreeSet<Integer> right) {
        while (left.size() > right.size()) {
            right.add(left.pollFirst());
        }
    }
    
    private double getMedian(int k, int[] nums, TreeSet<Integer> left, TreeSet<Integer> right) {
        if (k % 2 == 0) {
            return ((double) nums[left.first()] + nums[right.first()]) / 2;
        }
        else {
            return (double) nums[right.first()];
        }
    }
}
'''